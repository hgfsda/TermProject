import requests
import xml.etree.ElementTree as ET
from tkinter import *

url = 'https://openapi.gg.go.kr/Heatwaverestarere?KEY=47bd6dc9f9724cc787a3164da514a319&pIndex=1&pSize=1000'

def process(str, listbox):
    queryParams= {'SIGUN_NM': str}

    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)
    listbox.delete(0, END)

    row_count = 1
    for item in root.iter("row"):
        faclt = item.findtext("RESTARER_FACLT_NM")   # 쉼터명
        # typediv = item.findtext("RESTARER_TYPE_DIV_NM")  # 시설유형
        # area = item.findtext("FACLT_AR")   # 면적 (m^2)
        # pncnt = item.findtext("UTLZ_POSBL_PSNNUM_CNT")  # 이용가능인원수
        # elefancnt = item.findtext("ELEFAN_HOLD_CNT")   # 선풍기보유현황
        # arcndtncnt = item.findtext("ARCNDTN_HOLD_CNT")  # 에어컨보유현황
        # night = item.findtext("NIGHT_EXTS_OPERT_YN")  # 야간개방
        # wkend = item.findtext("WKEND_OPERT_YN")   # 휴일개방
        # syayng = item.findtext("STAYNG_POSBL_YN ")  # 숙박가능여부
        # partclr = item.findtext("PARTCLR_MATR")  # 특이사항
        # telno = item.findtext("MNGINST_TELNO")  # 관리기관전화번호
        # Lmna = item.findtext("REFINE_ROADNM_ADDR") # 소재지도로명주소
        # Lna = item.findtext("REFINE_LOTNO_ADDR") # 소재지지번주소
        # ZipCode = item.findtext("REFINE_ZIP_CD")     # 우편번호

        listbox.insert(row_count, faclt)
        row_count += 1

def processBookmark(str, listbox, Bookmarklistbox, shelters_data, bookmarklist):
    queryParams= {'SIGUN_NM': str}

    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)

    row_count = 1

    selected_indices = listbox.curselection()
    if not selected_indices:
        return
    selected_faclt = listbox.get(selected_indices[0])
    if selected_faclt in bookmarklist:
        print(1)
        bookmarklist.remove(selected_faclt)
        for i, shelter in enumerate(shelters_data):
            if shelter["faclt"] == selected_faclt:
                shelters_data.pop(i)
                break
        for i in range(Bookmarklistbox.size()):
            if Bookmarklistbox.get(i) == selected_faclt:
                Bookmarklistbox.delete(i)
                break
    else:
        for item in root.iter("row"):
            if item.findtext("RESTARER_FACLT_NM") == selected_faclt:
                shelter = {
                    "faclt":item.findtext("RESTARER_FACLT_NM"),  # 쉼터명
                    "typediv":item.findtext("RESTARER_TYPE_DIV_NM"),  # 시설유형
                    "area":item.findtext("FACLT_AR"),   # 면적 (m^2)
                    "pncnt":item.findtext("UTLZ_POSBL_PSNNUM_CNT"),  # 이용가능인원수
                    "elefancnt":item.findtext("ELEFAN_HOLD_CNT"),   # 선풍기보유현황
                    "arcndtncnt":item.findtext("ARCNDTN_HOLD_CNT"),  # 에어컨보유현황
                    "night":item.findtext("NIGHT_EXTS_OPERT_YN"),  # 야간개방
                    "wkend":item.findtext("WKEND_OPERT_YN"),   # 휴일개방
                    "syayng":item.findtext("STAYNG_POSBL_YN "),  # 숙박가능여부
                    "partclr":item.findtext("PARTCLR_MATR"),  # 특이사항
                    "telno":item.findtext("MNGINST_TELNO"),  # 관리기관전화번호
                    "Lmna":item.findtext("REFINE_ROADNM_ADDR"), # 소재지도로명주소
                    "Lna":item.findtext("REFINE_LOTNO_ADDR"), # 소재지지번주소
                    "ZipCode":item.findtext("REFINE_ZIP_CD")     # 우편번호
                }
                shelters_data.append(shelter)
                bookmarklist.append(shelter["faclt"])
                Bookmarklistbox.insert(END, shelter["faclt"])
                row_count += 1