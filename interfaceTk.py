#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from  tkinter import ttk

import time
import dateBase as dB

import os 
from alright import WhatsApp
from datetime import datetime

## SCRIPT ##
"""
Uses Selenium to send a text
"""
def dbReadListContats():
        return dB.Criar_lista_contatos()

ws  = Tk()
ws.title('Python Bot Send')
ws.geometry('550x900+400+50')


game_frame = Frame(ws)
game_frame.pack()


#labels


#scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set)



my_game.pack()

game_scroll.config(command=my_game.yview)

#define our column
 
my_game['columns'] = ('id', 'nome', 'contato')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("id",anchor=CENTER, width=140)
my_game.column("nome",anchor=CENTER,width=200)
my_game.column("contato",anchor=CENTER,width=140)


#Create Headings 
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("id",text="Nº",anchor=CENTER)
my_game.heading("nome",text="Nome",anchor=CENTER)
my_game.heading("contato",text="Contato",anchor=CENTER)


#add data 
contats = dbReadListContats()

for contats_index in contats.index:
    my_game.insert(parent='',index='end',iid=contats_index,text='',values=(contats_index+1,
    contats.at[contats_index,"Nome"],
    contats.at[contats_index,"Contato"]))

my_game.pack()


frame = Frame(ws)
frame.pack(pady=40, padx=40)

#labels
messageLabel = Label(frame,text = "Mensagem Padrão")
messageLabel.grid(row=0,column=0 )



#Entry boxes
messagemText_entry = Text(frame)
messagemText_entry.grid(row=1,column=0)

msg = open("mensagem.txt", encoding="utf8")
message = msg.read()
messagemText_entry.insert(END,message)


bar = Frame (ws)
bar.pack()


pb = ttk.Progressbar(bar, orient="horizontal", mode="indeterminate", length=280)
pb.grid(column=0,row=1,columnspan=2,padx=10,pady=20)



#Enviando mensagens aos filiados
def send_msg():
    list_contats = dB.Criar_lista_contatos()

    messager = WhatsApp()

    print (list_contats)
    
    pb.start()

    for i in list_contats.index:
        time.sleep(1)
        
        phone_no = list_contats.at[i,"Contato"]
        name_interesed = list_contats.at[i,"Nome"]

        
        print (phone_no, name_interesed)
        
        time.sleep(2)

        messager.find_user(phone_no)

        
        data_e_hora_em_texto = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        print(data_e_hora_em_texto)

        messager.send_message(
            "*{}* \n *_Olá, {}_'* \n {}".format(
                data_e_hora_em_texto,
                name_interesed,
                message)
                )
        
        time.sleep(2)

        
        os.chdir(r"C:\Users\maxso\Documents\Contabilidade Unidade Popular\Municipal\Pagamentos")
        print (os.getcwd())
        for i in os.listdir("."):
            messager.send_file(os.path.abspath(i))
            time.sleep(5)
    pb.stop()
   
    
    """  # Loads browser
    
    driver = sB.set_browser(sB.browser)
    

    for i in list_contats.index:
                time.sleep(1)
                
                phone_no = list_contats.at[i,"Contato"]
                name_interesed = list_contats.at[i,"Nome"]

                # Goes to site
                site = f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message.format(name=name_interesed))}"
                driver.get(site)
                element = lambda d : d.find_elements(by=By.XPATH, value="//div//button/span[@data-icon='send']")
                        
                time.sleep(4)
                # Waits until send is found (in case of login)
                loaded = WebDriverWait(driver, 1000).until(method=element, message="User never signed in")
                        
                # Loads a send button
                driver.implicitly_wait(10)
                send = element(driver)[0]
                        
                time.sleep(4)             
                # Clicks the send button
                send.click()     
                # Sleeps for 5 secs to allow time for text to send before closing window
                time.sleep(5)        
                
    # Closes windows
    driver.close() """

#Buttons
select_button = Button(ws,text="Enviar Cobrança", command=send_msg)
select_button.pack(pady =10)

ws.mainloop()