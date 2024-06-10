#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti


def replyAptData(user, loc_param='11710'):
    print(user, loc_param)
    res_list = noti.getData( loc_param)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '기간에 해당하는 데이터가 없습니다.')

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        noti.sendMessage( user, '저장되었습니다.' )
        conn.commit()

def check(user, bookmarklist):
    if bookmarklist:
        for shelter in bookmarklist:
            msg = (f"시설명 : {shelter['faclt']}\n"
                   f"시설유형 : {shelter['typediv']}\n"
                   f"면적(m²) : {shelter['area']}\n"
                   f"이용가능인원수 : {shelter['pncnt']}\n"
                   f"선풍기보유현황 : {shelter['elefancnt']}\n"
                   f"에어컨보유현황 : {shelter['arcndtncnt']}\n"
                   f"야간개방 : {shelter['night']}\n"
                   f"휴일개방 : {shelter['wkend']}\n"
                   f"숙박가능여부 : {shelter['syayng']}\n"
                   f"특이사항 : {shelter['partclr']}\n"
                   f"관리기관전화번호 : {shelter['telno']}\n"
                   f"소재지도로명주소 : {shelter['Lmna']}\n"
                   f"소재지지번주소 : {shelter['Lna']}\n"
                   f"우편번호 : {shelter['ZipCode']}\n\n")
            noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, "즐겨찾기 된 쉼터가 없습니다.")


def handle(msg, bookmarklist):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('지역') and len(args) > 1:
        replyAptData(chat_id, args[1])
    elif text.startswith('즐겨찾기'):
        check(chat_id, bookmarklist)
    else:
        noti.sendMessage(chat_id, "모르는 명령어입니다.\n다음과 같은 명령어를 입력해주십시오. \n1. 지역 [지역이름] \n2. 즐겨찾기")

def teller(bookmarklist):
    today = date.today()
    current_month = today.strftime('%Y%m')

    print('[', today, ']received token :', noti.TOKEN)

    bot = telepot.Bot(noti.TOKEN)
    pprint(bot.getMe())

    bot.message_loop(lambda msg: handle(msg, bookmarklist))