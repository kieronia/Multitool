import tkinter as tk
from tkinter import ttk
from tkinter import * 
import requests
from ping3 import ping, verbose_ping
import time
from colorama import init, Fore, Back, Style
blue='\033[44m'
red = "\e[0;31m"
init(convert=True)
def typeeffect(words):
    words
    for char in words:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def pingpong():
	ip = iptopingpong.get()
	while True:
		pingresponse = ping(ip)
		pingmilli = str(pingresponse)
		pingmilli = pingmilli[:5]

		if pingmilli == "False" or pingmilli == "None" or pingmilli =="Offline":
			print(red)
			typeeffect(f" > {ip} - HIT OFF!")
			

		else:
			print(blue)
			typeeffect(f' > Reply from {ip}: time={pingmilli}s')
			
		time.sleep(0.5)



root = Tk()

root.geometry('356x509')
root.configure(background='#999999')
root.title('Le python pingor')


iptopingpong=Entry(root)
iptopingpong.place(x=110, y=81)


Button(root, text='la ping le pong', bg='#97FFFF', font=('arial', 12, 'bold'), command=pingpong).place(x=110, y=120)



root.mainloop()
