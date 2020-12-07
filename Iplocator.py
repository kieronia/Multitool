import tkinter as tk
from tkinter import ttk
from tkinter import * 
import requests,os,time,threading,random
  
from colorama import Fore, init, Style

init(convert = True)
colors = [Fore.GREEN,Fore.RED,Fore.BLUE,Fore.YELLOW,Fore.WHITE,Fore.CYAN]

def typeeffect(locateresults):
	locateresults = locateresults.split()
	for words in locateresults:
    #words
		color = random.choice(colors)
		print(color)	
		for char in words:
			time.sleep(random.choice([0.05]))
			sys.stdout.write(char)
			sys.stdout.flush()
			#this looked cool so I added it :shrug:

os.system("title Ip Locator")
def locate():
	locatethis = ip.get()
	locateresults = requests.get(f"https://ipapi.co/{locatethis}/json/").text.replace('"',"")
	os.system("title Ip Located")
	locateresults = locateresults.replace(",","")
	junk = """
    postal: Sign up to access
    latitude: Sign up to access
    longitude: Sign up to access
"""
	locateresults = locateresults.replace(",","")
	locateresults = locateresults.replace(junk,"")
	locateresults = locateresults.replace("message: Please message us at ipapi.co/trial for full access","")
	locateresults = locateresults.replace("{","")
	locateresults = locateresults.replace("}","")
	Label(root, text=f"{locateresults}\n\n", bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=250, y=0)#originally the label covering the main bits needed to locate was an accident but then I thought it was pretty smooth and kept it that way :shrug:
	threading.Thread(target = typeeffect, args = (locateresults,)).start()


root = Tk()
root.geometry('756x520')
root.configure(background='#EE6AA7')
root.title('Ip locator')
ip=Entry(root)
ip.place(x=294, y=100)
Button(root, text='Locate', bg='#FFF0F5', font=('arial', 15, 'bold'), command=locate).place(x=313, y=126)
root.mainloop()
