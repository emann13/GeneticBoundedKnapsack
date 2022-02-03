from tkinter import *
from PIL import ImageTk, Image
import numpy as np
# from DEbounded import run
from tkinter import messagebox

# genetic_bounded
v = []
w = []
n = 0


def add():
    e = int(weight.get())
    w.append(e)
    e = int(value.get())
    v.append(e)


def addN():
    n = num.get()
    return n


def Wmax():
    maxWx = Mweight.get()
    return maxWx


def code():
    col = addN()
    col = int(col)
    maxW = Wmax()
    maxW = int(maxW)
    row = 10

    # generate the population matrix
    def population(r, cc):
        rand = np.random.randint(0, 2, (r, cc))
        addz = np.zeros((r, 4))
        rand = np.append(rand, addz, axis=1)
        return rand

    def validate_genome(g):
        su = 0
        for i in range(col):
            if np.round(g[i]) == 1:
                su += int(w[i])

            if su > maxW:
                return 0
        return su

    rand_pop = population(row, col)
    rand_popTemp = population(row, col)
    maxVal = 0
    cr = int(np.floor(0.80 * row))
    cm = int(np.ceil(0.20 * row))

    def SumValue(c1, v1) -> int:
        summ = 0
        for i in range(col):
            if rand_pop[c1, i] == 1:
                summ += int(v1[i])
                # print(sum,"\n")

        return summ

    for itr in range(200):

        for i in range(row):
            b = validate_genome(rand_pop[i, 0:col])
            Value = 0
            rand_pop[i, col] = b
            if b != 0:

                Value = int(SumValue(i, v))
                rand_pop[i, col + 1] = Value
                if Value > maxVal:
                    maxVal = Value
                    bestChrom = str(rand_pop[i, 0:col])
            else:
                Value = 0
                rand_pop[i, col + 1] = Value



            # print("\nBest Genome up:", bestChrom, "\nMaximum Value: ", maxVal)
        x = np.average(rand_pop[:, col + 1])

        # print(rand_pop)
        if x == 0:
            rand_pop = population(row, col)
            rand_popTemp = population(row, col)
            continue
        for i in range(row):
            rand_pop[i, col + 2] = rand_pop[i, col + 1] / x
            rand_pop[i, col + 3] = int(np.round(rand_pop[i, col + 2]))

            # Next generation formation

        count = 0
        c = 0
        for i in range(row):
            noc = rand_pop[i, col + 3]
            count += noc
            if count > row:
                noc -= 1
            for j in range(int(noc)):
                if c == row:
                    break
                rand_popTemp[c] = rand_pop[i, 0:col + 4]
                c += 1
        rand_pop[:, 0:col + 4] = rand_popTemp

        # print("\nThe next generation: \n", rand_pop[:, 0:col])
        # Crossover
        for i in range(cr):
            k = np.random.randint(0, col)
            r1 = np.random.randint(0, row)
            r2 = np.random.randint(0, row)
            a = rand_pop[r1, :col].tolist()
            b = rand_pop[r2, :col].tolist()

            cr1 = a[0:k] + b[k:col]
            cr2 = b[0:k] + a[k:col]

            rand_pop[r1, :col] = np.reshape(cr1, (1, col))
            rand_pop[r2, :col] = np.reshape(cr2, (1, col))
        # Mutation
        # np.reshape(x, (3, 2))
        for i in range(cm):
            rrow = np.random.randint(0, row)
            rcol = np.random.randint(0, col)
            rand_pop[rrow, rcol] = 1 - rand_pop[rrow, rcol]
        for i in range(row):
            b = validate_genome(rand_pop[i, 0:col])
            Value = 0
            rand_pop[i, col] = b
            if b != 0:

                Value = int(SumValue(i, v))
                rand_pop[i, col + 1] = Value
                if Value > maxVal:
                    maxVal = Value
                    bestChrom = str(rand_pop[i, 0:col])
            else:
                Value = 0
                rand_pop[i, col + 1] = Value

            # print("\nBest Genome last:", bestChrom, "\nMaximum Value: ", maxVal)

    # print("\nBest Genome itr:", bestChrom, "\nMaximum Value itr: ", maxVal)
    print("\nBest Genome:", bestChrom, "\nMaximum Value: ", maxVal)
    s1 = str(maxVal)
    s2 = str(bestChrom)
    s = str("Max Value: " + s1 + "  Best Chromosome:  " + s2 + " ")
    messagebox.showinfo("Solution", s)


def get_result():
    # not ready
    code()


screen = Tk()
screen.title('knapsack')
screen.geometry('800x500')
screen.config(bg='#D3D3D3')

screen.iconbitmap(r'knapsack.png')  # path of icon like D:/photos/Thief.ico
my_img = ImageTk.PhotoImage(Image.open(r'knapsack.png'))  # path of photo

my_label = Label(image=my_img)
my_label.pack()
addButton = Button(screen, text='Add Item', command=add)  # command is function that button will call
addButton.place(x=350, y=375)
bestkanp = Button(screen, text='best chromosome', command=get_result)
bestkanp.place(x=450, y=375)
addButton = Button(screen, text='enter number of items', command=addN)  # command is function that button will call
addButton.place(x=200, y=375)
# addButton.pack()
addButton = Button(screen, text='enter the max weight', command=Wmax)  # command is function that button will call
addButton.place(x=60, y=375)

#######################################################
l = Label(screen, text="weight", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=450, y=320)
weight = Entry(screen, width=15)
weight.place(x=450, y=350)
###########################################################
l = Label(screen, text="value", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=350, y=320)
value = Entry(screen, width=10)
value.place(x=350, y=350)
################################################

l = Label(screen, text="number of items", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=200, y=320)
num = Entry(screen, width=10)
num.place(x=200, y=350)
#######################################################

#######################################################
l = Label(screen, text="Max weight", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=70, y=320)
Mweight = Entry(screen, width=15)
Mweight.place(x=70, y=350)
screen.mainloop()

