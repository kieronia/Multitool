import json,requests,time
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import os



os.system("title Phone Number Locator (Get the country code)")






def magik():
	phonenumber = num.get()
	data = requests.get(f"https://api.telnyx.com/anonymous/v2/number_lookup/{phonenumber}").text.replace('"',"").replace(",","")
	data = data.split()
	#print(data[4])
	#print(data[2])
	Label(root, text=data[4], bg='#EE3B3B', font=('arial', 15, 'bold')).place(x=3, y=226)
	Label(root, text=data[2], bg='#EE3B3B', font=('arial', 25, 'bold')).place(x=6, y=256)




root = Tk()
root.geometry('305x520')
root.configure(background='#EE3B3B')
root.title('Phone Number')
num=Entry(root)
num.place(x=81, y=82)
Label(root, text='Number', bg='#EE3B3B', font=('arial', 15, 'bold')).place(x=106, y=48)
Button(root, text='Get The Country Code!', bg='#FFD39B', font=('arial', 10, 'bold'), command=magik).place(x=59, y=149)

root.mainloop()
