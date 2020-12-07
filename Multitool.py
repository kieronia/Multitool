import tkinter as tk
from tkinter import ttk
from tkinter import * 
import webbrowser
import subprocess
import time
import os
import threading
from colorama import init, Fore, Back, Style

init(convert=True)
os.system("cls")
os.system("title github.com/kieronia Multitool - Rebuild of tiktok.com/@misliking")
def run(program):
    os.system(f"{program}.py")    


def typeeffect(words):
    words
    for char in words:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def email():
	print(f'{Fore.CYAN} >{Fore.WHITE} Opening temp-mail.org')
	try:
		webbrowser.open("https://temp-mail.org/")
		print(f'{Fore.GREEN} >{Fore.WHITE} Opened temp-mail.org')
	except:
		print(f'{Fore.RED} >{Fore.WHITE} Error Opening temp-mail.org')









def hwid():
	print(f'{Fore.CYAN} >{Fore.WHITE} Getting Hwid')
	try:
		hwid = str(subprocess.check_output(
			'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
		print(f'{Fore.GREEN} >{Fore.WHITE} Success!')
		print(f'{Fore.GREEN} >{Fore.WHITE} Your Hwid : ')
		typeeffect(f" > {hwid}")
		print()
	except:
		print(f'{Fore.RED} >{Fore.WHITE} Error Getting Hwid')


def portsc():
	threading.Thread(target = run, args = ("PortScanner",)).start()

	#os.system("PortScanner.py")


def linkvertise():
	threading.Thread(target = run, args = ("Linkvertise",)).start()
	#os.system("Linkvertise.py")

def ping():
	threading.Thread(target = run, args = ("Pinger",)).start()
#	os.system("Pinger.py")


def smsrec():

	print(f'{Fore.CYAN} >{Fore.WHITE} Opening receive-smss.com')
	try:
		webbrowser.open("https://receive-smss.com/")
		print(f'{Fore.GREEN} >{Fore.WHITE} Opened receive-smss.com')
	except:
		print(f'{Fore.RED} >{Fore.WHITE} Error Opening receive-smss.com')




def visitthedev():
	print(f'{Fore.CYAN} >{Fore.WHITE} Opening github.com/kieronia')
	try:
		webbrowser.open("https://github.com/kieronia")
		print(f'{Fore.GREEN} >{Fore.WHITE} Opened github.com/kieronia')
	except:
		print(f'{Fore.RED} >{Fore.WHITE} Error Opening github.com/kieronia')



def visittheethicalhacker():
	print(f'{Fore.CYAN} >{Fore.WHITE} Opening tiktok.com/@misliking')
	try:
		webbrowser.open("https://www.tiktok.com/@misliking")
		print(f'{Fore.GREEN} >{Fore.WHITE} Opened tiktok.com/@misliking')
	except:
		print(f'{Fore.RED} >{Fore.WHITE} Error Opening tiktok.com/@misliking')



def proxies():
        threading.Thread(target = run, args = ("Proxyscraper",)).start()
	#os.system("Proxyscraper.py")

def phone():
	threading.Thread(target = run, args = ("Phonelocator",)).start()
	#os.system("Phonelocator.py")

def iploc():
	threading.Thread(target = run, args = ("Iplocator",)).start()
	#os.system("Iplocator.py")

root = Tk()
root.geometry('881x576')
root.configure(background='#7D26CD')
root.title('github.com/kieronia - Misliking Multitool Rebuild')



#Background= Canvas(root, height=881, width=576)
#picture_file = PhotoImage(file = 'Background.gif')  #u need the background gif in the same path if u wanna use this
#Background.create_image(881, 0, anchor=NE, image=picture_file)
#Background.place(x=3, y=4)
#Remove the tags for the neon sunset background as see in the tool - looks bad imo


Button(root, text='Temp Email', bg='#FFFAFA', font=('arial', 12, 'bold'), command=email).place(x=50, y=175) #command complete!
Button(root, text='Hwid', bg='#FFFAFA', font=('arial', 12, 'bold'), command=hwid).place(x=400, y=175) #command complete! Note : This is NOT a hwid spoofer - stuff like that isn't really possible in python, but it will print your current hwid
Button(root, text='Linkvertise Bypass', bg='#FFFAFA', font=('arial', 12, 'bold'), command=linkvertise).place(x=650, y=175)
#I felt smart doing this one (pretty simple but anyways) , since I've heard the linkvertise bypass in the tool didn't work, and the bypasser I've seen before had problems; https://online-coding.eu/api/LinkvertiseBypass.php?url= , I searched up linkvertise bypass and eventually found this website:https://thebypasser.com/ , this wasn't quite what I wanted as I needed an api but from monitoring the network requests, it was using someone else's api, this beauty: https://bigdonker.herokuapp.com/api?url=

Button(root, text='IP Lookup', bg='#FFFAFA', font=('arial', 12, 'bold'), command=iploc).place(x=50, y=300)#command complete!
Button(root, text='NMap Port Scanner', bg='#FFFAFA', font=('arial', 12, 'bold'), command=portsc).place(x=400, y=300)
Button(root, text='Phone Number Lookup', bg='#FFFAFA', font=('arial', 12, 'bold'), command=phone).place(x=650, y=300)#command complete!
Button(root, text='Proxy Scraper', bg='#FFFAFA', font=('arial', 12, 'bold'), command=proxies).place(x=50, y=425)#command in progress
Button(root, text='Pinger', bg='#FFFAFA', font=('arial', 12, 'bold'), command=ping).place(x=400, y=425)#command complete!
Button(root, text='Sms Reciever', bg='#FFFAFA', font=('arial', 12, 'bold'), command=smsrec).place(x=650, y=425)#command complete!

Button(root, text='Click Me To Visit The Dev', bg='#FFFAFA', font=('arial', 12, 'bold'), command=visitthedev).place(x=170, y=550)#command complete!
Button(root, text='Click Me To Visit Misliking', bg='#FFFAFA', font=('arial', 12, 'bold'), command=visittheethicalhacker).place(x=450, y=550)#command complete!


Label(root, text="Welcome To Kieronia's Tool", bg='#7D26CD', font=('arial', 45, 'normal')).place(x=78, y=5)#yes
Label(root, text='https://github.com/kieronia', bg='#7D26CD', font=('arial', 20, 'normal')).place(x=268, y=70)#yes


root.mainloop()
