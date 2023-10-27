from tkinter import *

def muda_imagem():
    nova_imagem = "imagens/" + escolha.get() + ".png"
    imagem["file"] = nova_imagem


fonte = ("Arial", "12")
window.tk()
window.title("Escolha seu Avatar")
window.geometry("400x200")
window.configure(bg="mocassin")

escolha = StringVar()
escolha.set("chaplin")

container1 = Frame(window, padx = 10, bg="mocassin")
container2 = Frame(window, padx = 10, bg="mocassin")

container1.pack(side=LEFT)
container2.pack(side=TOP)

texto = ["Charles Chaplin", "Harley Quinn", "Ninja do Deserto", "Copo do Zorro"]
valor = ["chaplin", "arlequina", "ninja", "zorro"]

for i in range(0,4,1):
    Radiobutton(container1, text=texto[i],
            value=valor[i], variable=escolha, width=15, acnhor="w",
            padx=10, pady=5, bg="mocassin",font=fonte,
            command=muda_imagem).pack()

radio_chaplin.pack()

imagem = PhotoImage(file="imagens/chaplin.png")
rotulo = Label(container2, image=imagem, bg="mocassin")
rotulo.pack()

window.mainloop()