from tkinter import *
from tkinter import font
import tkinter.ttk
from data import *

class main:
    def __init__(self):
        self.window = Tk(className="쉼터")
        self.notebook = tkinter.ttk.Notebook(self.window, width=700, height=500)
        self.notebook.pack()
        frame1 = self.frame1()
        self.notebook.add(frame1, text="메인")
        frame2 = self.frame2()
        self.notebook.add(frame2, text="쉼터 정보")
        frame3 = self.frame3()
        self.notebook.add(frame3, text="즐겨찾기")
        self.window.mainloop()

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

        return frame1

    def frame2(self):
        frame2 = Frame(self.window)
        Label(frame2, text="쉼터 정보 페이지", font='helvetica 48').pack()
        return frame2

    def frame3(self):
        frame3 = Frame(self.window)
        Label(frame3, text="즐겨찾기 페이지", font='helvetica 48').pack()
        return frame3



main()