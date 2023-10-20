# COMBOBOX

# combobox temos como definir uma lista de valores no qual podemos selecionar um
# Podemos uutilizar o combobox precisamo importa tudo do modulo tkinter.ttk 

# Nas chaves values indicamos os valres que teremos no combobox. Com a chave state podemos inidcar o valor 
# readonly para deixar o combobox  somente como leitura 

# Com a função corrent(indice) podemos definir um dos valores como o valor padrão(pelo seu indice)
# cOM A FUNÇÃO GET() podemos obter o valor o item selecionado no combobox

from tkinter.ttk import * #seguir essa ordem de importação
from tkinter import *

#criando função
def muda_imagem():
    nova_imagem = "img/" + combo.get() + ".png"
    imagem["file"] = nova_imagem

#criando janela
fonte = ("Cooper Black", "14")
window = Tk()
window.title("Escolha seu Avatar")
window.geometry("400x300")

#rptulo1
rotulo1 = Label(window, text="Escolha seu avatar", pady=20, font=fonte)
rotulo1.pack()
container1 = Frame(window, pady=20, padx=10)
container1.pack() #faz ele aparecer na janela

#Criando combobox
combo = Combobox(container1)
combo["values"] = ("Arlequina", "Chaplin", "Gueixa", "Ninja", "Zorro") #combo de infos
combo["state"] = "readonly" #apenas leitura
combo.current(0) #valor 0 é o indice da arlequina
combo.pack(side=LEFT)
imagem = PhotoImage(file="img/arlequina.png")

#rotulo2
rotulo2= Label(container1, image=imagem)
rotulo2.pack(side=RIGHT)
botao = Button(window, text="Muda o Avatar", pady=5, padx=10, font=fonte)
botao["command"] = muda_imagem
botao.pack()

window.mainloop()
