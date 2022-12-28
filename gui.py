from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text("Usuário"), sg.Input(key = 'usuario')],
    [sg.Text("Usuário"), sg.Input(key= 'senha', password_char='*')],
    [sg.Checkbox('Salvar o Login ?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'maxson' and valores['senha'] == '123456':
            print("OK")
            valores['usuario'] = ''
            valores['senha'] = '' 
