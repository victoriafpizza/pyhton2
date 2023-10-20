from tkinter import *
window = Tk ()
window.title("Titulo da Janela") #titulo da janela
window.geometry("350x2350") #tamanho da janela
window.configure(background="moccasin") #varias configurações
rotulo = Label(window)
rotulo["text"] = "Hello Word" #texto que esta escrito
rotulo["font"] = ("Impact", "20", "bold") # estilo da fonte
rotulo["fg"] = "brown" # cor da frente
rotulo["bg"] = "moccasin" # cor de fundo
rotulo["pady"] = 5
rotulo["padx"] = 10
rotulo["width"] = 20 #caracteres
rotulo["anchor"] = "w"

rotulo.pack()
window.mainloop()