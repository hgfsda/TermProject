import requests
import xml.etree.ElementTree as ET
import tkinter
#병원정보 서비스 예제
url = 'https://openapi.gg.go.kr/Heatwaverestarere?KEY=47bd6dc9f9724cc787a3164da514a319'
queryParams = {'SIGUN_NM': '시흥시'}

response = requests.get(url, params=queryParams)
print(response.text)
root = ET.fromstring(response.text)

window = tkinter.Tk()
window.title("쉼터정보")

frame = tkinter.Frame(window)
frame.pack()

header = ["name", "type", "Tel", "ar"]

for i, col_name in enumerate(header):
    label = tkinter.Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
    label.grid(row=0, column=i)

row_count = 1
for item in root.iter("row"):
    faclt = item.findtext("RESTARER_FACLT_NM")
    typediv = item.findtext("RESTARER_TYPE_DIV_NM")
    telno = item.findtext("MNGINST_TELNO")
    facltar = item.findtext("FACLT_AR")

    data = [faclt, typediv, telno, facltar]
    for i, value in enumerate(data):
        label = tkinter.Label(frame, text=value, font=("Helvetica", 12))
        label.grid(row=row_count, column=i)

    row_count += 1

window.mainloop()