import requests
import xml.etree.ElementTree as ET
from tkinter import *
import spam

url = 'https://openapi.gg.go.kr/Heatwaverestarere?KEY=47bd6dc9f9724cc787a3164da514a319&pIndex=1&pSize=1000'

def process(str, listbox, elementData):
    queryParams= {'SIGUN_NM': str}

    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)
    listbox.delete(0, END)

    row_count = 1
    for item in root.iter("row"):
        faclt = item.findtext("RESTARER_FACLT_NM")   # 쉼터명
        listbox.insert(row_count, faclt)
        row_count += 1

    for i in range(len(elementData)):
        elementData[i] = []

    for i, item in enumerate(root.iter("row")):
        if i >= 20:
            break
        elementData[0].append(item.findtext("RESTARER_FACLT_NM"))  # 쉼터명
        elementData[1].append(item.findtext("UTLZ_POSBL_PSNNUM_CNT"))  # 이용가능인원수
        elementData[2].append(item.findtext("FACLT_AR"))  # 면적 (m^2)
        elementData[3].append(item.findtext("ELEFAN_HOLD_CNT"))  # 선풍기보유현황
        elementData[4].append(item.findtext("ARCNDTN_HOLD_CNT"))  # 에어컨보유현황

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

def processMaps(str, listbox, map_widget):
    queryParams = {'SIGUN_NM': str}

    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)

    selected_indices = listbox.curselection()
    if not selected_indices:
        return
    selected_faclt = listbox.get(selected_indices[0])

    for item in root.iter("row"):
        if item.findtext("RESTARER_FACLT_NM") == selected_faclt:
            ZipCode = item.findtext("REFINE_ZIP_CD")  # 쉼터명
            map_widget.delete_all_marker()
            address = ZipCode + ", 대한민국"
            map_widget.set_address(address, marker=True)

            break


def processGmail(str, listbox):
    queryParams = {'SIGUN_NM': str}

    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)

    selected_indices = listbox.curselection()
    if not selected_indices:
        return
    shelters_data = []
    selected_faclt = listbox.get(selected_indices[0])
    for item in root.iter("row"):
        if item.findtext("RESTARER_FACLT_NM") == selected_faclt:
            shelter = {
                "faclt": item.findtext("RESTARER_FACLT_NM"),  # 쉼터명
                "typediv": item.findtext("RESTARER_TYPE_DIV_NM"),  # 시설유형
                "area": item.findtext("FACLT_AR"),  # 면적 (m^2)
                "pncnt": item.findtext("UTLZ_POSBL_PSNNUM_CNT"),  # 이용가능인원수
                "elefancnt": item.findtext("ELEFAN_HOLD_CNT"),  # 선풍기보유현황
                "arcndtncnt": item.findtext("ARCNDTN_HOLD_CNT"),  # 에어컨보유현황
                "night": item.findtext("NIGHT_EXTS_OPERT_YN"),  # 야간개방
                "wkend": item.findtext("WKEND_OPERT_YN"),  # 휴일개방
                "syayng": item.findtext("STAYNG_POSBL_YN "),  # 숙박가능여부
                "partclr": item.findtext("PARTCLR_MATR"),  # 특이사항
                "telno": item.findtext("MNGINST_TELNO"),  # 관리기관전화번호
                "Lmna": item.findtext("REFINE_ROADNM_ADDR"),  # 소재지도로명주소
                "Lna": item.findtext("REFINE_LOTNO_ADDR"),  # 소재지지번주소
                "ZipCode": item.findtext("REFINE_ZIP_CD")  # 우편번호
            }
            shelters_data.append(shelter)

    window = Tk(className="받을 메일 입력")
    window.geometry("250x70")
    recipientEntry = Entry(window, width=230)
    recipientEntry.place(x=0, y=10)
    recipientButton = Button(window, text="    전송    ", command=lambda:mailsend(recipientEntry, shelters_data))
    recipientButton.place(x=90, y=36)
    window.mainloop()


def mailsend(recipientEntry, shelters_data):
    host = "smtp.gmail.com"
    port = "587"
    title = "쉼터 정보"
    senderAddr = "jtyk119@tukorea.ac.kr"
    passwd = spam.getpw()
    recipientAddr = str(recipientEntry.get())

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgtext = ""
    for shelter in shelters_data:
        msgtext += (f"시설명 : {shelter['faclt']}\n"
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
    msgPart = MIMEText(msgtext, 'plain')
    msg.attach(msgPart)

    s = smtplib.SMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    def close_window():
        mail_window.destroy()

    mail_window = Tk(className="메일 전송")
    mail_window.geometry("240x100")
    l = Label(mail_window, text='메일을 전송하였습니다.')
    l.pack(pady=10)
    b = Button(mail_window, text='   확인   ', command=close_window)
    b.pack(pady=10)
    mail_window.mainloop()

