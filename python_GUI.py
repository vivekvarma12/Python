from tkinter import *
import subprocess
def open():
    w=e.get()
	    if w=="notepad" or w=="n++"  or w=="note++":
	        subprocess.Popen([r"C:\Program Files (x86)\Notepad++\notepad++.exe"])
		    elif w=="chrome" or w=="google" or w=="gchrome":
			        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
			    elif w=="fox" or w=="ffox" or w=="mfox":
		        subprocess.Popen([r"C:\Program Files\Mozilla Firefox\firefox.exe"])
					    elif w=="beans"  or w=="netb" or w=="nbeans":
						        subprocess.Popen([r"C:\Program Files\NetBeans 8.2\bin\netbeans64.exe"])
						    else:
							        m=Tk()
								    m.geometry("150x60")
								    Label(m,text="enter a valid application").grid(row=1,column=3)
								    m.mainloop()
						        #print("Enter a valid application")

master = Tk()
master.title("cortona daddy")
master.geometry("300x250")
master.configure(bg="cyan")
Label(master,text="Give your Application name :",bg="cyan").grid(row=3,column=5)
e=Entry(master)
e.grid(row=3,column=6)
Button(master, text='open', width=5, command=open).grid(row=4,column=6)
master.mainloop()
