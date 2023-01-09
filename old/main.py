from old.gui import *
from old.TransactionObject import *

app = None

def view_command():
    rows = view()
    app.listFiliados.delete(0, END)
    for r in rows:
        app.listFiliados.insert(END, r)

def search_command():
    app.listFiliados.delete(0, END)
    rows = search(app.txtNome.get(), app.txtContato.get(), app.txtMunicipio.get())
    for r in rows:
        app.listFiliados.insert(END, r)

def insert_command():
    insert(app.txtNome.get(), app.txtContato.get(), app.txtMunicipio.get())
    view_command()

def update_command():
    update(selected[0],app.txtNome.get(), app.txtContato.get(), app.txtMunicipio.get())
    view_command()

def del_command():
    id = selected[0]
    delete(id)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listFiliados.curselection()[0]
    selected = app.listFiliados.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entContato.delete(0, END)
    app.entContato.insert(END, selected[2])
    app.entMunicipio.delete(0, END)
    app.entMunicipio.insert(END, selected[3])
    
    return selected


if __name__ == "__main__":
    app = Gui()
    
    app.listFiliados.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
