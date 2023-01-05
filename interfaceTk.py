from tkinter import *
from  tkinter import ttk

from tkinter.messagebox import showinfo

from unicodedata import name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from re import fullmatch

from bot_msg import botSendMensage, dbReadListContats

import time
import dateBase as dB
import setBrowser as sB


## SCRIPT ##
"""
Uses Selenium to send a text
"""
def dbReadListContats():
        return dB.Criar_lista_contatos()

ws  = Tk()
ws.title('Python Bot Send')
ws.geometry('1200x800+400+100')


game_frame = Frame(ws)
game_frame.pack()


#labels


#scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)



my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

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
messageLabel = Label(frame,text = "Mensagem")
messageLabel.grid(row=0,column=0 )


#Entry boxes
messagemText_entry = Text(frame)
messagemText_entry.grid(row=1,column=0)

msg = open("mensagem.txt", encoding="utf8")
message = msg.read()
messagemText_entry.insert(END,message)

#Enviando mensagens aos filiados
def send_msg():
    list_contats = dB.Criar_lista_contatos()
    # Loads browser
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
    driver.close()
    
    """ 
    #grab record
    selected=my_game.focus()
    #grab record values
    values = my_game.item(selected,'values')
    #temp_label.config(text=selected)
"""
"""   #output to entry boxes
    playerid_entry.insert(0,values[0])
    playername_entry.insert(0,values[1])
    playerrank_entry.insert(0,values[2]) """

""" #save Record
def update_record():
    selected=my_game.focus()
    #save new data 
    my_game.item(selected,text="",values=(playerid_entry.get(),playername_entry.get(),playerrank_entry.get()))
    
   #clear entry boxes
    playerid_entry.delete(0,END)
    playername_entry.delete(0,END)
    playerrank_entry.delete(0,END)
 """
#Buttons
select_button = Button(ws,text="Enviar Cobrança", command=send_msg)
select_button.pack(pady =10)



""" 
refresh_button = Button(ws,text="Refresh Record",command=update_record)
refresh_button.pack(pady = 10) """

ws.mainloop()