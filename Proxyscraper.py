import tkinter as tk
from tkinter import ttk
from tkinter import * 
from colorama import init, Fore, Back, Style
import requests

init(convert=True)


def httpproxies():
	
	print(f"{Fore.CYAN} > {Fore.WHITE}Scraping HTTP Proxies")
	finalfilename = filename.get()
	finalfilename = finalfilename.replace(".txt","")#if they input .txt itd name it .txt.txt otherwise
	proxies = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all", allow_redirects=True)
 
	if finalfilename == "":  
		open('http.txt', 'wb').write(proxies.content)
	else:
		open(f'{finalfilename}.txt', 'wb').write(proxies.content)


def sockfour():
	print(f"{Fore.CYAN} > {Fore.WHITE}Scraping SOCK4 Proxies")
	finalfilename = filename.get()
	finalfilename = finalfilename.replace(".txt","")#if they input .txt itd name it .txt.txt otherwise
	proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all', allow_redirects=True)
 
	if finalfilename == "":  
		open('sock4.txt', 'wb').write(proxies.content)
	else:
		open(f'{finalfilename}.txt', 'wb').write(proxies.content)


def sockfive():
	print(f"{Fore.CYAN} > {Fore.WHITE}Scraping SOCK5 Proxies")
	finalfilename = filename.get()
	finalfilename = finalfilename.replace(".txt","")#if they input .txt itd name it .txt.txt otherwise
	proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all', allow_redirects=True)
 
	if finalfilename == "":  
		open('sock5.txt', 'wb').write(proxies.content)
	else:
		open(f'{finalfilename}.txt', 'wb').write(proxies.content)



root = Tk()

root.geometry('732x435')
root.configure(background='#6E8B3D')
root.title('Proxy Scraperrr')


Label(root, text='File name?', bg='#6E8B3D', font=('arial', 12, 'normal')).place(x=299, y=166)


filename=Entry(root)
filename.place(x=274, y=189)


Button(root, text='HTTP', bg='#FF4500', font=('arial', 12, 'bold'), command=httpproxies).place(x=55, y=305)


Button(root, text='SOCK4', bg='#00EE00', font=('arial', 12, 'bold'), command=sockfour).place(x=287, y=303)


Button(root, text='SOCK5', bg='#00FFFF', font=('arial', 12, 'bold'), command=sockfive).place(x=525, y=306)


root.mainloop()
