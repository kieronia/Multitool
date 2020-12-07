import requests
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import os
os.system("title Port Scanner")
def scan():
	os.system("title Port Scanning")
	iplel = Port.get()
	results = requests.get(f"https://api.hackertarget.com/nmap/?q={iplel}").text
	os.system("title Port Scanned")
	print(f"{results}\n\n")
	Label(root, text=results, bg='#EE3B3B', font=('arial', 15, 'bold')).place(x=100, y=20)







root = Tk()

root.geometry('870x543')
root.configure(background='#FFFACD')
root.title('PortScanner')


Port=Entry(root)
Port.place(x=333, y=73)


Label(root, text='Ip To Portscan:', bg='#FFFACD', font=('arial', 12, 'bold')).place(x=333, y=33)

Button(root, text='Scan', bg='#EEDC82', font=('arial', 25, 'bold'), command=scan).place(x=333, y=117)


root.mainloop()












