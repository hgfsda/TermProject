from tkinter import *
import tkinter.ttk

class main:
    window = Tk(className="쉼터")
    notebook = tkinter.ttk.Notebook(window, width=800, height=600)
    notebook.pack()

    frame1 = Frame(window)
    notebook.add(frame1, text="메인")
    Label(frame1, text="메인 페이지", font='helvetica 48').pack()

    frame2 = Frame(window)
    notebook.add(frame2, text="쉼터 정보")
    Label(frame2, text="쉼터 정보 페이지", font='helvetica 48').pack()

    frame3 = Frame(window)
    notebook.add(frame3, text="즐겨찾기")
    Label(frame3, text="즐겨찾기 페이지", font='helvetica 48').pack()

    window.mainloop()

main()