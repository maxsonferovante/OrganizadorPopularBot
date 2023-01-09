import os

os.chdir(r"C:\Users\maxso\Documents\Contabilidade Unidade Popular\Municipal\Extratos Caixa")

print (os.getcwd())

for i in os.listdir("."):
    print (os.path.abspath(i))

print(    "*{}* \n *_Olá, {}_'* \n {}".format(
                "asdasdasdasd",
                "aaaaaaaaaaa",
                "111111111111111")
                )
        