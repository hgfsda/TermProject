#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

TOKEN = '7243574633:AAGJtDBSAgpz3XJIp1NYYVrouC-bOEW7vR0'
MAX_MSG_LENGTH = 300
baseurl = 'https://openapi.gg.go.kr/Heatwaverestarere?KEY=47bd6dc9f9724cc787a3164da514a319&pIndex=1&pSize=1000'
bot = telepot.Bot(TOKEN)

def getData(loc_param):
    res_list = []
    encoded_loc_param = quote(loc_param)
    url = baseurl + '&SIGUN_NM=' + encoded_loc_param
    res_body = urlopen(url).read()
    soup = BeautifulSoup(res_body, 'html.parser')
    items = soup.findAll('row')
    for item in items:
        shelter_info = {}
        shelter_info['RESTARER_FACLT_NM'] = item.find('restarer_faclt_nm').text
        shelter_info['RESTARER_TYPE_DIV_NM'] = item.find('restarer_type_div_nm').text
        shelter_info['REFINE_ROADNM_ADDR'] = item.find('refine_roadnm_addr').text
        shelter_info['REFINE_ZIP_CD'] = item.find('refine_zip_cd').text

        # 조합된 문자열 생성
        formatted_info = f"{shelter_info['RESTARER_FACLT_NM']}, {shelter_info['RESTARER_TYPE_DIV_NM']}, {shelter_info['REFINE_ROADNM_ADDR']}, {shelter_info['REFINE_ZIP_CD']}"

        res_list.append(formatted_info)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData(param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user, log) VALUES (?, ?)', (user, r))
            except sqlite3.IntegrityError:
                pass
            else:
                print(str(datetime.now()).split('.')[0], r)
                if len(r + msg) + 1 > MAX_MSG_LENGTH:
                    sendMessage(user, msg)
                    msg = r + '\n'
                else:
                    msg += r + '\n'
        if msg:
            sendMessage(user, msg)
    conn.commit()

if __name__ == '__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print('[', today, ']received token :', TOKEN)

    pprint(bot.getMe())

    run(current_month)
