from tkinter import *
window = Tk ()
window.title("Titulo da Janela") #titulo da janela
window.geometry("350x2350") #tamanho da janela
window.configure(background="moccasin") #varias configurações
rotulo = Label(window, font="Impact 20 bold", bg="moccasin") #definindo fonte no label
rotulo["text"] = "Hello Word" #texto que esta escrito
rotulo.pack()
botao = Button(window, text="Click Me", padx=10, pady=10)
botao["font"] = ("Times New Roman", "16", "bold")
botao["fg"] = "white"
botao["bg"] = "black"
botao["command"] = window.destroy
botao.pack()
window.mainloop()