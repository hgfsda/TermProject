import requests
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import font
#병원정보 서비스 예제
url = 'https://openapi.gg.go.kr/Heatwaverestarere?KEY=47bd6dc9f9724cc787a3164da514a319'
queryParams = {'SIGUN_NM': '시흥시'}

response = requests.get(url, params=queryParams)
root = ET.fromstring(response.text)

window = Tk()
window.title("쉼터정보")
window.geometry("700x500")

frame = Frame(window)
frame.pack()

TempFont = font.Font(window, size=10, family='Consolas')
ShelterListBox = Listbox(window, font=TempFont, activestyle='none',
                         width=40, height=22, borderwidth=3, relief='ridge')

row_count = 1
for item in root.iter("row"):
    faclt = item.findtext("RESTARER_FACLT_NM")
    typediv = item.findtext("RESTARER_TYPE_DIV_NM")
    telno = item.findtext("MNGINST_TELNO")
    facltar = item.findtext("FACLT_AR")

    ShelterListBox.insert(row_count, faclt)
    row_count += 1

ShelterListBox.pack()
ShelterListBox.place(x=10, y=110)

window.mainloop()