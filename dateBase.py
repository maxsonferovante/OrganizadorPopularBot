from ast import Pass
from audioop import mul
import pandas as pd
import os
from re import fullmatch

"""
Functions that do self explanatory tasks
"""
def modify_number(phone_no):

    def check_number(number):
        if "55" in number[:2]:
            return number
        return "55" + number

    phone_no = str(phone_no).replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("+","")
   
    return check_number(number=phone_no)

def validate_number(phone_no):

    if fullmatch(r"^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$", phone_no):
        raise Exception("Invalid Phone Number.")
    return True

# Filtrar lista do excel, remove todas as linhas que não possuam o valor "filtro" na "col_filt"
def Format_Numb (lf):

    for num_a in lf['Contato']:
        aux = num_a
 
        num_a = modify_number(num_a)
 
        lf = lf.replace(to_replace =aux, value = num_a )
    return lf    


# Obter dados do excel
def Criar_lista_contatos ():
    print(os.getcwd())
    lista_contatos = Format_Numb(pd.read_excel("base.xlsx"))
    return lista_contatos

print(os.getcwd())
