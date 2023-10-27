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

radio_chaplin = Radiobutton(container1, text="Charles Chaplin",
            value="chaplin", variable=escolha, width=15, acnhor="w",
            padx=10, pady=5, bg="mocassin",font=fonte,
            command=muda_imagem)

radio_quinn = Radiobutton(container1, text="Harley Quinn",
            value="arlequina", variable=escolha, width=15, acnhor="w",
            padx=10, pady=5, bg="mocassin",font=fonte,
            command=muda_imagem)

radio_ninja = Radiobutton(container1, text="Ninja do Deserto",
            value="ninja", variable=escolha, width=15, acnhor="w",
            padx=10, pady=5, bg="mocassin",font=fonte,
            command=muda_imagem)

radio_zorro = Radiobutton(container1, text="Copo do Zorro",
            value="zorro", variable=escolha, width=15, acnhor="w",
            padx=10, pady=5, bg="mocassin",font=fonte,
            command=muda_imagem)

radio_chaplin.pack()
radio_quinn.pack()
radio_ninja.pack()
radio_zorro.pack()

imagem = PhotoImage(file="imagens/chaplin.png")
rotulo = Label(container2, image=imagem, bg="mocassin")
rotulo.pack()

window.mainloop()