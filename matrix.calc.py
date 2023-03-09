from tkinter import *
import tkinter as tk
from tkinter.tix import *
from tkinter import ttk
import tkinter.font as tkFont


root = tk.Tk()
root.geometry('600x400')

root.title('Matrix.calc')
dr = '#BCBCEE'
col1 = '#BCBCEE'
#col = '#EEE8AA'
col = '#C1C1CD'
root['bg'] = dr




my_canvas = tk.Canvas(root, bg=dr)

frameF = Frame(width=300, height = 200, bg = dr)

frameF.pack(side = BOTTOM, pady = 2)

my_scrollbar1 = tk.Scrollbar(root,orient = "horizontal")
my_scrollbar1.pack(side = "bottom", fill = "x", expand = True)

my_scrollbar = tk.Scrollbar(root, orient = 'vertical')
my_scrollbar.pack(side = "right", fill = "y")


my_canvas.pack(side = TOP,fill=BOTH, expand = True)






frameW = tk.Frame(my_canvas,width = 1000, height = 1000, bg = dr)
frameW.grid(column = 1)
frame4 = tk.Frame(frameW,width = 300, height = 200,bg = dr)
frame4.grid(column = 0, row = 0)
frame5 = tk.Frame(frameW,width = 200, height = 200, bg = dr)
frame5.grid(column = 1, row = 0, padx = 12)




my_canvas.configure(yscrollcommand = my_scrollbar.set, xscrollcommand = my_scrollbar1.set)

my_canvas.create_window((0, 0),anchor = 'n', window = frameW)


root['bg'] = dr
matrix1 = []
matrix2 = []
catrix1 = []
catrix2 = []
resultts = []
resultt = []




frame1 = Frame(frameF,width=200, height = 200, bg = dr)
frame2 = Frame(frameF,width=200, height = 200, bg = dr)
frame3 = Frame(frameF,width=200, height = 200, bg = dr)

frame1.pack(side=LEFT)
frame2.pack(side=LEFT)
frame3.pack(side = BOTTOM)












my_scrollbar.configure(command = my_canvas.yview)
my_scrollbar1.configure(command = my_canvas.xview)



lbls = tk.Label(frame5, text = 'Ответ:')
lblt = tk.Label(frame4, bg = dr, text = ' ')
lblt.grid(row=500, column = 0)


def clickII(event, obj):
    if obj.get() == '0':
        obj.delete(0, END)

def otvet():
        for i in range(len(resultt)):
            trs = []
            for j in range(len(resultt[0])):
                lbl = tk.Label(frame5, text = resultt[i][j], width = 3)
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
            entry = tk.Entry(frame4, width=4)
            entry.grid(row=i, column=j)
            entry.insert(0, 0)
            entry.bind("<1>", lambda event, obj=entry: clickII(event, obj))
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
            entry = tk.Entry(frame4, width=4)
            entry.grid(row=i+1000, column=j)
            entry.bind("<1>", lambda event, obj=entry: clickII(event, obj))
            row.append(entry)
            entry.insert(0, 0)
        matrix2.append(row)
    lbls.grid_forget()
def copy1():
    clearm1()
    for i in range(len(resultt)):
        row = []
        for j in range(len(resultt[i])):
            entry = tk.Entry(frame4, width=4)
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
            entry = tk.Entry(frame4, width=4)
            entry.grid(row=i+1000, column=j)
            entry.bind("<1>", lambda event, obj=entry: clickII(event, obj))
            row.append(entry)
            entry.insert(0, resultt[i][j])
        matrix2.append(row)


def callback():
    lbl
    return True


entry1 = tk.Entry(frame1, width=5)
entry1.grid(row = 1, column = 1, pady = 1)

lble1 = tk.Label(frame1, text = 'Кол-во столбцов')
lble1.grid(row = 1, column = 2,pady = 1)

entry2 = tk.Entry(frame1, width=5)
entry2.grid(row = 2, column = 1, pady = 1)

lble2 = tk.Label(frame1, text = 'Кол-во строк')
lble2.grid(row = 2, column = 2, pady = 1)

entry3 = tk.Entry(frame2,width=5)
entry3.grid(row = 1, column = 1, pady = 1)

lble3 = tk.Label(frame2, text = 'Кол-во столбцов')
lble3.grid(row = 1, column = 2, pady = 1)

entry4 = tk.Entry(frame2, width=5)
entry4.grid(row = 2, column = 1, pady = 1)

lble4 = tk.Label(frame2, text = 'Кол-во строк')
lble4.grid(row = 2, column = 2, pady = 1)

button_add1 = tk.Button(frame1, text="Добавить первую матрицу", command=add1, bg = col)
button_add1.grid(row = 3, column = 1, columnspan=2, pady = 1)

button_add2 = tk.Button(frame2, text="Добавить вторую матрицу", command=add2, bg = col)
button_add2.grid(row = 3, column = 1, columnspan=2, pady = 1)

add = tk.Button(frame3, text="+", command=plus, width=5,height=1, bg = col)
add.grid(row = 1, column = 1)

add1 = tk.Button(frame3, text="-", command=minus, width=5,height=1, bg = col)
add1.grid(row = 1, column = 2)

add2 = tk.Button(frame3, text="*", command=matmult, width=5,height=1, bg = col)
add2.grid(row = 2, column = 1)

button_copy1 = tk.Button(frame3, text="Результат -> 1 матрицу",command=copy1, bg = col)
button_copy1.grid(row = 1, column = 3, pady = 1, padx = 3)

button_copy2 = tk.Button(frame3, text="Результат -> 2 матрицу",command=copy2, bg = col)
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
add3 = tk.Button(frame3, text="Очистить", command=cleara, bg = col)
add3.grid(row = 3, column = 1, columnspan = 2)


def adjust_scrollregion(event):
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))
frameW.bind("<Configure>", adjust_scrollregion)
my_canvas.bind("<Configure>", adjust_scrollregion)

root.mainloop()


