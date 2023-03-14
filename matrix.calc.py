from tkinter import *
import tkinter as tk
import customtkinter as ct
import numpy as np
from numpy.linalg import inv
from functools import partial
import time

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

root = ct.CTk()
root.geometry('700x500')

root.title('Matrix.calc')

frameF = ct.CTkFrame(root,width=300, height = 200)
frameF.pack(side = BOTTOM, pady = 2)
frameW = ct.CTkScrollableFrame(root)
frameW.pack(side = TOP, fill = BOTH, expand=True)
frame4 = ct.CTkFrame(frameW,width = 400, height = 400)
frame4.grid(column = 0, row = 0)
frame5 = ct.CTkFrame(frameW,width = 650, height = 200)
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
    resultts.clear()
    for i in range(len(resultt)):
        trs = []
        for j in range(len(resultt[0])):
            lbl = ct.CTkLabel(frame5, text = resultt[i][j], width = 35, fg_color="gray22", corner_radius=3)
            lbl.grid(row=i+1, column=j, padx = 1, pady = 1)
            trs.append(lbl)
        resultts.append(trs)
        lbls.grid(row=0, column=0, columnspan = 1000, pady = 10)
def plus():
    global resultt
    clearc()
    clearr()
    unit()
    if len(catrix1) == len(catrix2) and len(catrix1[0]) == len(catrix2[0]):
        for i in range(len(catrix1)):
            srt = []
            for j in range(len(catrix1[0])):
                stri = catrix1[i][j] + catrix2[i][j]
                srt.append(stri)
            resultt.append(srt)
    else:
        lbls.grid_forget()
    otvet()
def minus():
    clearc()
    clearr()
    unit()
    srt = []
    if len(catrix1) == len(catrix2) and len(catrix1[0]) == len(catrix2[0]):
        for i in range(len(catrix1)):
            srt = []
            for j in range(len(catrix1[0])):
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
    global catrix1, catrix2
    clearc()
    if len(matrix1) != 0:
        for i in range(len(matrix1)):
            gg = []
            for j in range(len(matrix1[0])):
                try:
                    gg.append(int(matrix1[i][j].get()))
                except ValueError:
                    gg.append(0)
            catrix1.append(gg)
    if len(matrix2) != 0:
        for i in range(len(matrix2)):
            ss = []
            for j in range(len(matrix2[0])):
                try:
                    ss.append(int(matrix2[i][j].get()))
                except:
                    ss.append(0)
            catrix2.append(ss)
def addM(mat, AorB):
    clearm(mat)
    clearr()
    if mat == matrix1 and AorB == True:
        a = int(entry1.get())
        b = int(entry2.get())
    elif mat == matrix2 and AorB == False:
        a = int(entry3.get())
        b = int(entry4.get())
    else:
        return
    for i in range(a):
        row = []
        for j in range(b):
            entry = ct.CTkEntry(frame4, width=35, placeholder_text = 0)
            if mat == matrix1 and AorB == True:
                entry.grid(row=i, column=j)
            elif mat == matrix2:
                entry.grid(row=i+1000, column=j)
            row.append(entry)
        mat.append(row)
    lbls.grid_forget()
def copy(matr, sda):
    clearm(matr)
    for i in range(len(resultt)):
        row = []
        for j in range(len(resultt[0])):
            entry = ct.CTkEntry(frame4, width=35, placeholder_text = 0)
            if matr == matrix1 and sda == True:
                entry.grid(row=i, column=j)
            elif matr == matrix2 and sda == False:
                entry.grid(row=i+1000, column=j)
            if resultt[i][j] != 0:
                entry.insert(0,int(resultt[i][j]))
            row.append(entry)
        matr.append(row)
def tran(catrix):
    global resultt
    clearr()
    clearc()
    unit()
    a = catrix
    catri = np.array(a)
    resultt = catri.transpose().tolist()
    otvet()
def inver():
    global catrix1, resultt
    clearr()
    clearc()
    unit()
    a = catrix1
    catrix = np.array(a)
    resultt = np.around(inv(a), decimals=3).tolist()
    otvet()
def mest():
    global resultt
    unit()
    c = resultt
    a = catrix1
    b = catrix2
    resultt = b
    copy(matrix1, True)
    resultt = a
    copy(matrix2, False)
    clearc()
    resultt = c

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

lble3 = ct.CTkLabel(frame2, text = 'Кол-во столбцов', width = 125)
lble3.grid(row = 1, column = 2, pady = 1)

entry4 = ct.CTkEntry(frame2, width=30)
entry4.grid(row = 2, column = 1, pady = 1)

lble4 = ct.CTkLabel(frame2, text = 'Кол-во строк')
lble4.grid(row = 2, column = 2, pady = 1)

button_add1 = ct.CTkButton(frame1, text="Добавить 1-ую матрицу", command=partial(addM, matrix1, True), width = 170)
button_add1.grid(row = 3, column = 1, columnspan=2)

button_add2 = ct.CTkButton(frame2, text="Добавить 2-ую матрицу", command=partial(addM, matrix2, False), width = 170)
button_add2.grid(row = 3, column = 1, columnspan=2)

add = ct.CTkButton(frame3, text="+", command=plus, width=55,height=34)
add.grid(row = 0, column = 1)

add1 = ct.CTkButton(frame3, text="-", command=minus, width=55,height=34)
add1.grid(row = 1, column = 1)

add2 = ct.CTkButton(frame3, text="*", command=matmult, width=55,height=34)
add2.grid(row = 2, column = 1)

add5 = ct.CTkButton(frame1, text="Найти обратную", command=inver, width=170,height=10)
add5.grid(row = 5, column = 1, columnspan = 2)

add6 = ct.CTkButton(frame1, text="Транспонировать", command=partial(tran, catrix1), width=170,height=10,)
add6.grid(row = 4, column = 1, columnspan = 2)

add7 = ct.CTkButton(frame2, text="Найти обратную", command=inver, width=170,height=10)
add7.grid(row = 5, column = 1, columnspan = 2)

add8 = ct.CTkButton(frame2, text="Транспонировать", command=partial(tran, catrix2), width=170,height=10)
add8.grid(row = 4, column = 1,pady = 1, columnspan = 2)

button_change = ct.CTkButton(frame3, text="Поменять местами", command=mest)
button_change.grid(row = 0, column = 3, pady = 1, padx = 3)

button_copy1 = ct.CTkButton(frame3, text="Результат -> 1 матрицу",command=partial(copy, matrix1, True))
button_copy1.grid(row = 1, column = 3, pady = 1, padx = 3)

button_copy2 = ct.CTkButton(frame3, text="Результат -> 2 матрицу",command=partial(copy, matrix2, False))
button_copy2.grid(row = 2, column = 3, pady = 1, padx = 3)

def cleara():
    clearm(matrix1)
    clearm(matrix2)
    clearr()
    lbls.grid_forget()
def clearm(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j].destroy()
    mat.clear()
def clearr():
    global resultt, resultts
    for i in range(len(resultts)):
        for j in range(len(resultts[0])):
            resultts[i][j].destroy()
    resultts.clear()
    resultt.clear()
add3 = ct.CTkButton(frame3, text="Очистить", command=cleara, width = 100)
add3.grid(row = 3, column = 3, columnspan = 2)
def clearc():
    catrix1.clear()
    catrix2.clear()
root.mainloop()