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

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('거래') and len(args) > 1:
        pass
    elif text.startswith('지역') and len(args)>1:
        print('try to 지역', args[1])
        replyAptData( chat_id, args[1] )
    else:
        noti.sendMessage(chat_id, """모르는 명령어입니다.\n거래 [YYYYMM] [지역번호] \n지역 [지역번호] \n저장 [지역번호] 
        \n확인 중 하나의 명령을 입력하세요.\n    지역 ["종로구 11110", "중구 11140", "용산구 11170", "성동구 11200", "광진구 11215"
        , "동대문구 11230", "중랑구 11260", "성북구 11290", "강북구 11305", "도봉구 11320", "노원구 11350", "은평구 11380", 
        "서대문구 11410", "마포구 11440", "양천구 11470", "강서구 11500", "구로구 11530", "금천구 11545", "영등포구 11560", 
        "동작구 11590", "관악구 11620", "서초구 11650", "강남구 11680", "송파구 11710", "강동구 11740"] """)


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)