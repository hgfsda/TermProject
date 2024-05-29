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

    def refreshBookmarks(self):
        self.BookmarkListBox.delete(0, END)
        for faclt in self.bookmarklist:
            self.BookmarkListBox.insert(END, faclt)

    def deleteBookmarks(self):
        selected_indices = self.BookmarkListBox.curselection()
        if selected_indices:
            selected_faclt = self.BookmarkListBox.get(selected_indices[0])
            if selected_faclt in self.bookmarklist:
                self.bookmarklist.remove(selected_faclt)
                for i, shelter in enumerate(self.shelters_data):
                    if shelter["faclt"] == selected_faclt:
                        self.shelters_data.pop(i)
                        break
                self.refreshBookmarks()

    def searchBookmark(self):
        selected_indices = self.BookmarkListBox.curselection()
        if selected_indices:
            selected_faclt = self.BookmarkListBox.get(selected_indices[0])
            for shelter in self.shelters_data:
                if shelter["faclt"] == selected_faclt:
                    self.displayData(shelter)
                    break

    def displayData(self, shelter):
        self.infoLabel.config(text=f"시설명: {shelter['faclt']}\n"
                                   f"시설유형: {shelter['typediv']}\n"
                                   f"면적(m^2): {shelter['area']}\n"
                                   f"이용가능인원수: {shelter['pncnt']}\n"
                                   f"선풍기보유현황: {shelter['elefancnt']}\n"
                                   f"에어컨보유현황: {shelter['arcndtncnt']}\n"
                                   f"야간개방: {shelter['night']}\n"
                                   f"휴일개방: {shelter['wkend']}\n"
                                   f"숙박가능여부: {shelter['syayng']}\n"
                                   f"특이사항: {shelter['partclr']}\n"
                                   f"관리기관전화번호: {shelter['telno']}\n"
                                   f"소재지도로명주소: {shelter['Lmna']}\n"
                                   f"소재지지번주소: {shelter['Lna']}\n"
                                   f"우편번호: {shelter['ZipCode']}")

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
        bookmarkButton = Button(frame1, image=self.bookmark,
                                command=lambda:processBookmark(NameEntry.get(), ShelterListBox,
                                                               self.BookmarkListBox, self.shelters_data, self.bookmarklist))
        bookmarkButton.place(x=300,y=280)
        self.maps = PhotoImage(file="image/googleMaps.png")
        bookmarkButton = Button(frame1, image=self.maps, command=lambda:processMaps(NameEntry.get(),ShelterListBox,
                                                                                    self.map_widget))
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
        title = Label(frame3, text="즐겨찾기", font='helvetica 48')
        title.place(x=10, y=10)
        TempFont = font.Font(self.window, size=10, family='Consolas')
        self.BookmarkListBox = Listbox(frame3, font=TempFont, activestyle='none',
                                 width=40, height=22, borderwidth=3, relief='ridge')
        self.BookmarkListBox.place(x=10, y=100)
        checkB = Button(frame3, text='  검색  ', command=self.searchBookmark)
        checkB.place(x=180, y=465)
        deleteB = Button(frame3, text='  제거  ', command=self.deleteBookmarks)
        deleteB.place(x=245, y=465)
        self.infoLabel = Label(frame3, bg='white',borderwidth=4,font=TempFont, justify=LEFT)
        self.infoLabel.place(x=310, y=100)
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
        self.shelters_data = []

        self.window.mainloop()

main()