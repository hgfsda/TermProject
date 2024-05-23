import requests
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import font
#병원정보 서비스 예제
window = Tk()
window.title("쉼터정보")
window.geometry("700x500")

url = 'https://openapi.gg.go.kr/Heatwaverestarere?KEY=47bd6dc9f9724cc787a3164da514a319&pIndex=1&pSize1000'

def process():
    dollar = NameEntry.get()
    queryParams['SIGUN_NM'] = dollar

    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)
    ShelterListBox.delete(0, END)

    row_count = 1
    for item in root.iter("row"):
        faclt = item.findtext("RESTARER_FACLT_NM")   # 쉼터명
        typediv = item.findtext("RESTARER_TYPE_DIV_NM")  # 시설유형
        area = item.findtext("FACLT_AR")   # 면적 (m^2)
        pncnt = item.findtext("UTLZ_POSBL_PSNNUM_CNT")  # 이용가능인원수
        elefancnt = item.findtext("ELEFAN_HOLD_CNT")   # 선풍기보유현황
        arcndtncnt = item.findtext("ARCNDTN_HOLD_CNT")  # 에어컨보유현황
        night = item.findtext("NIGHT_EXTS_OPERT_YN")  # 야간개방
        wkend = item.findtext("WKEND_OPERT_YN")   # 휴일개방
        syayng = item.findtext("STAYNG_POSBL_YN ")  # 숙박가능여부
        partclr = item.findtext("PARTCLR_MATR")  # 특이사항
        telno = item.findtext("MNGINST_TELNO")  # 관리기관전화번호
        latitude = item.findtext("REFINE_WGS84_LAT")  # 위도
        hardness = item.findtext("REFINE_WGS84_LOGT")  # 경도


        ShelterListBox.insert(row_count, faclt)
        row_count += 1

NameEntry = Entry(window)
NameEntry.pack()
NameEntry.place(x=10, y=80)

queryParams = {}
b1 = Button(window, text='검색', command=process)
b1.place(x=160, y= 80)


frame = Frame(window)
frame.pack()

TempFont = font.Font(window, size=10, family='Consolas')
ShelterListBox = Listbox(window, font=TempFont, activestyle='none',
                         width=40, height=22, borderwidth=3, relief='ridge')

ShelterListBox.pack()
ShelterListBox.place(x=10, y=110)

window.mainloop()