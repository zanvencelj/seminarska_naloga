import smtplib
from smtplib import SMTPException
from email.message import EmailMessage
import tkinter as tk
from tkinter import *
import pandas as pd
from openpyxl import load_workbook
import time
import os

xl = pd.ExcelFile('maili.xlsx')
maili = xl.parse('maili')

def send():
    x = 0
    ST = maili['st'][0]
    mojmail = moj_mail.get()
    mojegeslo = moje_geslo.get()
    while x < ST:
        msg = EmailMessage()
        msg['Subject'] = 'KAM PO KARTUŠE? - BREZPLAČNA DOSTAVA KARTUŠ IN TONERJEV' # Primer naslova
        msg['From'] = mojmail
        msg['To'] =  maili['maili'][x]
    
        msg.set_content('Oglas')
        msg.add_alternative("""\
        
        
        #tukaj pride oblika HTML za vsebino!
        
        
        """, subtype='html')
    
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(mojmail,mojegeslo)
        
        #besedilo.config(state="normal")
    
        try:
            server.send_message(msg)
            print('Mail poslan na ' + maili['maili'][x])
            
        except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
            besedilo.insert(tk.END, 'Sporočilo ni bilo poslano')
            
        finally:
            server.quit()
            
        x += 1
        time.sleep(1)
        #besedilo.config(state="disabled")

root = tk.Tk()

def donothing():
    print('Menubar is not set yet!')

def openFile():
    os.startfile('maili.xlsx')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

canvas = tk.Frame(root, height=100, width=700, bg="#333")
canvas.pack()

vpisi_mail= tk.Label(root, text='Vnesite svoj Gmail naslov: ')
vpisi_mail.pack()
vpisi_mail.config(bg='#333', fg='#fff')

moj_mail= tk.Entry(root)
moj_mail.pack()
moj_mail.config(bg='#95a5a6', fg='#2c3e50', width=50)

vpisi_mail= tk.Label(root, text='Vnesite svoje geslo za Gmail: ')
vpisi_mail.pack()
vpisi_mail.config(bg='#333', fg='#fff')

moje_geslo= tk.Entry(root, show='*', width=50)
moje_geslo.insert(END, '********')
moje_geslo.pack()
moje_geslo.config(bg='#95a5a6', fg='#2c3e50')

edat= Button(root, text='Odpri Excel', command=openFile)
edat.pack(padx=5, pady=20, ipadx=115,)
edat.config(bg='#95a5a6')

poslji= Button(root, text='Pošlji!', command=send)
poslji.pack(padx=5, pady=10, ipadx=6, ipady=2)
poslji.config(bg='#95a5a6')

canvas = tk.Frame(root, height=100, width=700, bg="#333")
canvas.pack()

root.config(menu=menubar, bg='#333')
root.title("Pošiljanje mailov")
root.iconbitmap('./vencelj.ico')
root.mainloop()