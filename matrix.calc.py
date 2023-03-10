from tkinter import *
import tkinter as tk
import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

root = ct.CTk()
root.geometry('700x400')



root.title('Matrix.calc')



frameF = ct.CTkFrame(root,width=300, height = 200)
frameF.pack(side = BOTTOM, pady = 2)

frameW = ct.CTkScrollableFrame(root)
frameW.pack(side = TOP, fill = BOTH, expand=True)
frame4 = ct.CTkFrame(frameW,width = 400, height = 400)
frame4.grid(column = 0, row = 0)
frame5 = ct.CTkFrame(frameW,width = 650, height = 400)
frame5.grid(column = 1, row = 0, padx = 12, sticky='n')


matrix1 = []
matrix2 = []
catrix1 = []
catrix2 = []
resultts = []
resultt = []

frame1 = ct.CTkFrame(frameF,width=200, height = 200)
frame2 = ct.CTkFrame(frameF,width=200, height = 200)
frame3 = ct.CTkFrame(frameF,width=200, height = 200)

frame1.pack(side=LEFT)
frame2.pack(side=LEFT)
frame3.pack(side = BOTTOM)

lbls = ct.CTkLabel(frame5, text = 'Ответ:')
lblt = ct.CTkLabel(frame4,text = ' ')
lblt.grid(row=500, column = 0)

def otvet():
        for i in range(len(resultt)):
            trs = []
            for j in range(len(resultt[0])):
                lbl = ct.CTkLabel(frame5, text = resultt[i][j], width = 35, fg_color="gray75", corner_radius=3)
                lbl.grid(row=i+1, column=j, padx = 1, pady = 1)
                trs.append(lbl)
            resultts.append(trs)
            lbls.grid(row=0, column=0, columnspan = 1000, pady = 10)
def plus():
    global c, d
    clearr()
    unit()
    if a == c and b == d:
        for i in range(a):
            srt = []
            for j in range(b):
                stri = catrix1[i][j] + catrix2[i][j]
                srt.append(stri)
            resultt.append(srt)
    else:
        print('err')
        lbls.grid_forget()
        
    otvet()
def minus():
    global a, b
    clearr()
    unit()
    srt = []
    if a == c and b == d:
        for i in range(a):
            srt = []
            for j in range(b):
                stri = catrix1[i][j] - catrix2[i][j]
                srt.append(stri)
            resultt.append(srt)
    else:
        lbls.grid_forget()
    otvet()
def matmult():
    clearr()
    unit()
    if len(catrix1) == len(catrix2[0]):
        r=[]
        for i in range(len(catrix1)):
            for j in range(len(catrix2[0])):
                sums=0
                for k in range(len(catrix2)):
                    sums=sums+(catrix1[i][k]*catrix2[k][j])
                r.append(sums)
            resultt.append(r)
            r=[]
        otvet()

def unit():
    for i in range(a):
        gg = []
        for j in range(b):
            try:
                gg.append(int(matrix1[i][j].get()))
            except ValueError:
                gg.append(0)
        catrix1.append(gg)
    for i in range(c):
        gg = []
        for j in range(d):
            try:
                gg.append(int(matrix2[i][j].get()))
            except:
                gg.append(0)
        catrix2.append(gg)
def add1():
    clearm1()
    clearr()
    global a, b
    a = int(entry1.get())
    b = int(entry2.get())
    for i in range(a):
        row = []
        for j in range(b):
            entry = ct.CTkEntry(frame4, width=35, placeholder_text = 0)
            entry.grid(row=i, column=j)
            row.append(entry)
        matrix1.append(row)
    lbls.grid_forget()
def add2():
    clearr()
    clearm2()
    global c, d
    c = int(entry3.get())
    d = int(entry4.get())
    for i in range(c):
        row = []
        for j in range(d):
            entry = ct.CTkEntry(frame4, width=35, placeholder_text = 0)
            entry.grid(row=i+1000, column=j)
            row.append(entry)
        matrix2.append(row)
    lbls.grid_forget()
def copy1():
    clearm1()
    for i in range(len(resultt)):
        row = []
        for j in range(len(resultt[i])):
            entry = ct.CTkEntry(frame4, width=4)
            entry.grid(row=i, column=j)
            entry.bind("<1>", lambda event, obj=entry: clickII(event, obj))
            row.append(entry)
            entry.insert(0, resultt[i][j])
        matrix1.append(row)
def copy2():
    clearm2()
    for i in range(len(resultt)):
        row = []
        for j in range(len(resultt[i])):
            entry = ct.CTkEntry(frame4, width=4)
            entry.grid(row=i+1000, column=j)
            entry.bind("<1>", lambda event, obj=entry: clickII(event, obj))
            row.append(entry)
            entry.insert(0, resultt[i][j])
        matrix2.append(row)


def callback():
    lbl
    return True


entry1 = ct.CTkEntry(frame1, width=30)
entry1.grid(row = 1, column = 1, pady = 1)

lble1 = ct.CTkLabel(frame1, text = 'Кол-во столбцов')
lble1.grid(row = 1, column = 2,pady = 1)

entry2 = ct.CTkEntry(frame1, width=30)
entry2.grid(row = 2, column = 1, pady = 1)

lble2 = ct.CTkLabel(frame1, text = 'Кол-во строк')
lble2.grid(row = 2, column = 2, pady = 1)

entry3 = ct.CTkEntry(frame2,width=30)
entry3.grid(row = 1, column = 1, pady = 1)

lble3 = ct.CTkLabel(frame2, text = 'Кол-во столбцов')
lble3.grid(row = 1, column = 2, pady = 1)

entry4 = ct.CTkEntry(frame2, width=30)
entry4.grid(row = 2, column = 1, pady = 1)

lble4 = ct.CTkLabel(frame2, text = 'Кол-во строк')
lble4.grid(row = 2, column = 2, pady = 1)

button_add1 = ct.CTkButton(frame1, text="Добавить 1-ую матрицу", command=add1)
button_add1.grid(row = 3, column = 1, columnspan=2, pady = 1)

button_add2 = ct.CTkButton(frame2, text="Добавить 2-ую матрицу", command=add2)
button_add2.grid(row = 3, column = 1, columnspan=2, pady = 1, padx = 5)

add = ct.CTkButton(frame3, text="+", command=plus, width=52,height=10)
add.grid(row = 1, column = 1)

add1 = ct.CTkButton(frame3, text="-", command=minus, width=52,height=10)
add1.grid(row = 1, column = 2)

add2 = ct.CTkButton(frame3, text="*", command=matmult, width=52,height=10)
add2.grid(row = 2, column = 1)

button_copy1 = ct.CTkButton(frame3, text="Результат -> 1 матрицу",command=copy1)
button_copy1.grid(row = 1, column = 3, pady = 1, padx = 3)

button_copy2 = ct.CTkButton(frame3, text="Результат -> 2 матрицу",command=copy2)
button_copy2.grid(row = 2, column = 3, pady = 1, padx = 3)

def cleara():
    clearm1()
    clearm2()
    clearr()
    lbls.grid_forget()
def clearm1():
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix1[i][j].destroy()
    matrix1.clear()
def clearm2():
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            matrix2[i][j].destroy()
    matrix2.clear()
def clearr():
    for i in range(len(resultts)):
        for j in range(len(resultts[0])):
            resultts[i][j].destroy()
    resultts.clear()
    resultt.clear()
    catrix1.clear()
    catrix2.clear()
add3 = ct.CTkButton(frame3, text="Очистить", command=cleara, width = 100)
add3.grid(row = 3, column = 1, columnspan = 2)

root.mainloop()

