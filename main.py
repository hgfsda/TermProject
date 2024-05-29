from tkinter import *
from tkinter import font
import tkinter.ttk
from data import *
from tkintermapview import TkinterMapView


class main:
    def processGmail(self):
        pass

    def processTelegram(self):
        pass

    def processBookmark(self, listbox):
        selected_indices = listbox.curselection()  # 선택된 항목의 인덱스 가져오기
        if selected_indices:
            selected_faclt = listbox.get(selected_indices[0])  # 선택된 항목의 이름 가져오기
            if selected_faclt in self.bookmarklist:
                self.bookmarklist.remove(selected_faclt)
                print(self.bookmarklist)
            else:
                self.bookmarklist.append(selected_faclt)
                print(self.bookmarklist)


    def processMaps(self):
        pass

    def frame1(self):
        frame1 = Frame(self.window)
        self.notebook.add(frame1, text="메인")
        title = Label(frame1, text="쉼터", font='helvetica 48')
        title.place(x=10, y=10)

        NameEntry = Entry(frame1)
        NameEntry.place(x=10, y=90)

        TempFont = font.Font(self.window, size=10, family='Consolas')
        ShelterListBox = Listbox(frame1, font=TempFont, activestyle='none',
                                 width=40, height=22, borderwidth=3, relief='ridge')
        ShelterListBox.place(x=10, y=120)

        b1 = Button(frame1, text='검색', command=lambda:process(NameEntry.get(), ShelterListBox))
        b1.place(x=160, y=90)

        # 기능 버튼
        self.gmail = PhotoImage(file="image/Gmail.png")
        gmailButton = Button(frame1, image=self.gmail, command=self.processGmail)
        gmailButton.place(x=300,y=120)
        self.telegram = PhotoImage(file="image/Telegram.png")
        telegramButton = Button(frame1, image=self.telegram, command=self.processTelegram)
        telegramButton.place(x=300,y=200)
        self.bookmark = PhotoImage(file="image/Bookmark.png")
        bookmarkButton = Button(frame1, image=self.bookmark, command=lambda: self.processBookmark(ShelterListBox))
        bookmarkButton.place(x=300,y=280)
        self.maps = PhotoImage(file="image/googleMaps.png")
        bookmarkButton = Button(frame1, image=self.maps, command=self.processMaps)
        bookmarkButton.place(x=300,y=360)

        # 지도
        self.map_widget = TkinterMapView(width=400, height=400, corner_radius=0)
        self.map_widget.place(x=390, y=120)
        self.map_widget.set_address("Seoul, South Korea")

        return frame1

    def frame2(self):
        elementList = ['사용인원가능수', '면적(m^2)', '선풍기보유현황','에어컨보유현황']
        frame2 = Frame(self.window)
        el_combo = tkinter.ttk.Combobox(frame2, values=list(elementList))
        el_combo.place(x=5, y=10)
        return frame2

    def frame3(self):
        frame3 = Frame(self.window)
        Label(frame3, text="즐겨찾기 페이지", font='helvetica 48').pack()
        return frame3

    def __init__(self):
        self.window = Tk(className="쉼터")
        self.notebook = tkinter.ttk.Notebook(self.window, width=800, height=500)
        self.notebook.pack()
        frame1 = self.frame1()
        self.notebook.add(frame1, text="메인")
        frame2 = self.frame2()
        self.notebook.add(frame2, text="쉼터 정보")
        frame3 = self.frame3()
        self.notebook.add(frame3, text="즐겨찾기")

        self.bookmarklist = []

        self.window.mainloop()

main()