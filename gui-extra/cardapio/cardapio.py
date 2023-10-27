# Monte um programa onde o usuário pod escolher seu lanche, porção e bebida. Ao clicar em Fazer Pedido,
# exiba as imagens da escolha dele e exiba o total a ser pago (o valor escolha do Combobox tem valor R$ no preco)

from tkinter.ttk import * 
from tkinter import *

def muda_lanches():
    nova_imagem = "lanches/" + lanches.get() + ".png"
    imagem["file"] = nova_imagem

def muda_porcoes():
    nova_imagem = "porcoes/" + porcoes.get() + ".png"
    imagem["file"] = nova_imagem

def muda_bebidas():
    nova_imagem = "bebidas/" + bebidas.get() + ".png"
    imagem["file"] = nova_imagem

# fazer função para calculo do pedido

window = Tk()
window.title("Escolha seu Lanche, Porção e Bebida")
window.geometry("400x300")

lanches = Combobox(container1)
lanches["values"] = ("burger", "noodles", "pizza")
lanches["state"] = "readonly"
lanches.current(0)
lanches.pack(side=TOP)
imagem = PhotoImage(file="img/burger.png")
container1 = Frame(window, pady=20, padx=10)
container1.pack()

#PORÇÕES
porcoes = Combobox(container2)
porcoes["values"] = ("fritas", "nuggets", "milho")
porcoes["state"] = "readonly"
porcoes.current(0)
porcoes.pack(side=TOP)
imagem = PhotoImage(file="img/burger.png")
container2 = Frame(window, pady=20, padx=10)
container2.pack()

#BEBIDAS
bebidas = Combobox(container3)
bebidas["values"] = ("suco", "shake")
bebidas["state"] = "readonly"
bebidas.current(0)
bebidas.pack(side=TOP)
imagem = PhotoImage(file="img/burger.png")
container3 = Frame(window, pady=20, padx=10)
container3.pack()

#botao
botao = Button(window, text="Fazer Pedido", padx=10, pady=10)
botao["font"] = ("Times New Roman", "16", "bold")
botao["command"] = calculo_do_pedido
botao.pack()

window.mainloop()
