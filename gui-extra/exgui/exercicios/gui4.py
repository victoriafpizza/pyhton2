from tkinter import *

def muda_texto():
    rotulo1["text"] += caixa_texto.get()

window = Tk()
window.title("Boas Vindas")
window.geometry("450x200+400+200")

rotulo1 = Label(window, text="Seja bem Vindo!", font="Impact 20 bold", pady=10)
rotulo1.pack()

container =  Frame(window, pady=15, padx=10)
container.pack()

rotulo2 = Label(container, text="Nome", font="Imapct 16", pady=10)
rotulo2.pack(side=LEFT)

caixa_texto = Entry(container, font=("Times New Roman", "16"))
caixa_texto.pack(side=RIGHT)

botao = Button(window, text="Clique aqui", pady=5, padx=10, bg="black", fg="white")
botao["font"] = ("Courier New", "16", "bold")
botao["command"] = muda_texto
botao.pack()

caixa_texto.focus()
window.mainloop()