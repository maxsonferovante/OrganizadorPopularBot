from tkinter import *

class Gui():
    """Classe que define a interface gráfica da aplicação
    """
    #Criando a janela...
    window          = Tk()
    window.wm_title("Finanças UP PA")
    window.geometry('640x480+400+50')
     #Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtNome         = StringVar()
    
    txtContato        = StringVar()
    txtMunicipio          = StringVar()

     #Criando os objetos que estarão na janela...
    lblNome        = Label(window, text="Nome Completo (Nome Social)")
    lblContato       = Label(window, text="Contato")
    lblMunicipio         = Label(window, text="Municipio")

    listFiliados   = Listbox(window)
    scrollFiliados = Scrollbar(window)

    btnViewAll     = Button(window, text="Ver todos")
    btnBuscar      = Button(window, text="Buscar")
    btnInserir     = Button(window, text="Inserir")
    btnUpdate      = Button(window, text="Atualizar Selecionados")
    btnDel         = Button(window, text="Deletar Selecionados")
    btnClose       = Button(window, text="Fechar")

    entNome        = Entry(window, textvariable=txtNome)
    entContato       = Entry(window, textvariable=txtContato)
    entMunicipio     = Entry(window, textvariable=txtMunicipio)

    #Associando os objetos a grid da janela...
    lblNome.grid(row=0,column=0)
    
    lblContato.grid(row=2,column=0)
    lblMunicipio.grid(row=3, column=0)

    entNome.grid(row=0, column=1, padx=50, pady=50)
    
    entContato.grid(row=2, column=1)
    entMunicipio.grid(row=3, column=1)
    listFiliados.grid(row=0, column=2, rowspan=10)
    scrollFiliados.grid(row=0, column=6, rowspan=10)
    
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    listFiliados.configure(yscrollcommand=scrollFiliados.set)
    scrollFiliados.configure(command=listFiliados.yview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

     #Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def run(self):
        Gui.window.mainloop()