from tkinter import *
import subprocess
import xlrd
data=xlrd.open_workbook(r"C:\Users\vidoddip\Desktop\Programs_data.xlsx")
data1=data.sheet_by_index(0)
def open():
    w=var.get()
	    t=""
	    for i in range(data1.nrows):
		          if w == data1.cell_value(i,0):
			            t=data1.cell_value(i,1)
			            break
	    subprocess.Popen(t)
		
master = Tk()
master.title("cortona daddy")
master.geometry("300x250")
master.configure(bg="cyan")
l=[]
for i in range(data1.nrows):
   l.append(data1.cell_value(i,0))


var=StringVar(master)
var.set(l[0])
Label(master,text="Give your Application name :",bg="cyan").grid(row=3,column=5)
e=OptionMenu(master,var,*l)
e.grid(row=3,column=6)
Button(master, text='open', width=5, command=open).grid(row=5,column=6)
master.mainloop()
