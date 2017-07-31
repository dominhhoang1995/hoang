import Tkinter
from Tkinter import *
import tkMessageBox

ds = []
def chinh():
    rootA = Tk()
    rootA.title('Sap xep Quicksort')
    rootA.resizable(width=False, height=False)
    rootA.geometry('400x650')
    global listds

    label = Label(rootA, text="Sap xep Quicksort ", fg = "blue" , font = "Times 20 bold")
    label.pack()

    lbds = Label(rootA, text='Nhap danh sach : ' , fg = "blue", font = "Times 20 bold" )
    lbds.pack(side = TOP , padx=10 ,pady=10)
    listds = Entry(rootA)
    listds.pack(side = TOP , padx=20 ,pady=10)

    btnadd = Button(rootA, text="Them", fg="red", font = "Times 20 bold",command=danhsach)
    btnadd.pack(side = TOP , padx=10 ,pady=10)


    lbdssx = Label(rootA, text=' danh sach can sap xep la : ' , fg = "blue", font = "Times 20 bold")
    lbdssx.pack(side = TOP , padx=10 ,pady=10)

    global var2
    var2 = StringVar()
    lbkq1 = Label(rootA, textvariable=var2, relief=RAISED , fg = "red" ,font = "Times 20 bold")
    lbkq1.pack(side = TOP , padx=10 ,pady=10)

    btnsx = Button(rootA, text="Sap xep", fg="red", font = "Times 20 bold",command=sapxep)
    btnsx.pack(side = TOP , padx=40 ,pady=10)

    lbdssx = Label(rootA, text=' danh sach da sap xep la : ' , fg = "blue",font = "Times 20 bold")
    lbdssx.pack(side = TOP , padx=10 ,pady=10)

    global var
    var = StringVar()
    lbkq = Label(rootA, textvariable=var, relief=RAISED , fg = "red",font = "Times 20 bold" )
    lbkq.pack(side = TOP , padx=10 ,pady=10)
   
    btnclear = Button(rootA, text="CLEAR", fg="red", font = "Times 20 bold",command=clear)
    btnclear.pack(side = TOP , padx=10 ,pady=10)

    label = Label(rootA, text="Thuat Toan Sap xep Quicksort-Do Minh Hoang ", fg = "blue" , font = "Times 13 bold")
    label.pack(side = TOP , padx=10 ,pady=10)

    rootA.mainloop()


def clear():
    var2.set("")
    var.set("")
    del ds[:]
def danhsach():
    try:
      i = int(listds.get())
      ds.append(i)
      var2.set(ds)
    except ValueError:
         tkMessageBox.showinfo( "","ban nhap khong dung dinh dang. Vui long nhap lai! ")


def sapxep():
    quicksort(ds, 0, len(ds) - 1)
    var.set(ds)

def quicksort(mylist, sIndex, eIndex):
    # Neu chi co mot phan tu hoac eIndex < sIndex

    if eIndex <= sIndex:
        return
    else:
        # lưu giá trị phần tử giữa mảng
        pivot = mylist[int((eIndex + sIndex) / 2)]

        i = sIndex; # i chay tu trai sang phai
        j = eIndex; # j chay tu phai sang trai

        while i < j :
            # tim phan tu nam sai vi tri theo i
            while mylist[i] < pivot and i <= j:
                i += 1
             # tim phan tu nam sai vi tri theo j
            while mylist[j] > pivot and j >= i:
                j -= 1
          #neu i nam truoc j thi hoan vi
            if i < j:
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp
                i += 1
                j -= 1
            else:
                break

        if i == j:
            if mylist[i] <= pivot:
                quicksort(mylist, sIndex, i)
                quicksort(mylist, i + 1, eIndex)
            else:
                quicksort(mylist, sIndex, i - 1)
                quicksort(mylist, i, eIndex)
        else:
            quicksort(mylist, sIndex, j)
            quicksort(mylist, i, eIndex)

chinh()    
