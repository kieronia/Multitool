import tkinter as tk
from tkinter import ttk
from tkinter import * 
import requests
from colorama import init, Fore, Back, Style

init(convert=True)
def shorten():
	makeProgress()
	try:
		finalurl = linkverlink.get()
		thelink = requests.get(f"https://bigdonker.herokuapp.com/api?url={finalurl}").text
		makeProgress()
		#print(thelink)

		if thelink.lower() == "no url given":
			Label(root, text='You forgot to supply a link to bypass!', bg='#FAEBD7', font=('courier', 15, 'bold')).place(x=25, y=284)
			print(f"{Fore.RED} > {Fore.WHITE}Please supply a link")
		elif thelink.lower() == "invalid Linkvertise link. could not fetch data":
			Label(root, text='Please Supply A VALID Link!', bg='#FAEBD7', font=('courier', 15, 'bold')).place(x=25, y=284)
			print(f"{Fore.RED} >{Fore.WHITE} Please supply a valid linkvertise link")

		elif thelink.lower() == "this website is not supported":
			Label(root, text="Error - Website Isn't Supported", bg='#FAEBD7', font=('courier', 15, 'bold')).place(x=25, y=284)
			print(f" {Fore.RED}>{Fore.WHITE} Website Not Supported")

		elif thelink.lower() == "invalid url":
			Label(root, text="Please supply a valid url", bg='#FAEBD7', font=('courier', 15, 'bold')).place(x=25, y=284)
			print(f" {Fore.RED}> {Fore.WHITE}Invalid Url :|")

		else:
			#shortened = requests.get(f"https://tinyurl.com/api-create.php?url={thelink}").text  #I shorten it as it gets printed on the screen - imagine tryna type a mega.nz link out from that kek
			#Label(root, text=f'Shortened Link : {shortened}', bg='#FAEBD7', font=('courier', 10, 'bold')).place(x=12, y=284) #literally crashed my pc so remove the "#" if your pc can handle it
			

			Label(root, text=f'{thelink}', bg='#FAEBD7', font=('courier', 10, 'bold')).place(x=12, y=284) 
			print(f" {Fore.CYAN}>{Fore.WHITE} Link Recieved")
			print(f"{Fore.GREEN} >{Fore.WHITE} {thelink}")
		makeProgress()
		makeProgress()
		makeProgress()
	except:
		print(f" {Fore.RED}> {Fore.WHITE}Error")




def makeProgress():
	Progress['value']=Progress['value'] + 1
	root.update_idletasks()



root = Tk()

root.geometry('522x356')
root.configure(background='#FAEBD7')
root.title('Linkvertise Bypasser :)')


linkverlink=Entry(root)
linkverlink.place(x=199, y=112)


Label(root, text='Link?', bg='#FAEBD7', font=('courier', 20, 'bold')).place(x=220, y=70)


Progress_style = ttk.Style()
Progress_style.theme_use('clam')
Progress_style.configure('Progress.Horizontal.TProgressbar', foreground='#76EEC6', background='#76EEC6')


Progress=ttk.Progressbar(root, style='Progress.Horizontal.TProgressbar', orient='horizontal', length=129, mode='determinate', maximum=5, value=1)
Progress.place(x=199, y=183)


Button(root, text='Shorten', bg='#0000CD', font=('courier', 20, 'bold'), command=shorten).place(x=191, y=204)

root.mainloop()
