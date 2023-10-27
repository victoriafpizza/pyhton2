from tkinter import *

#declarando varivale de verificar pertences
def verifica_pertences():
    if tv.get():
        mensagem += "\n" + check_tv["text"]
    if tv.get():
        mensagem += "\n" + check_tv["text"]
    if tv.get():
        mensagem += "\n" + check_tv["text"]
    if tv.get():
        mensagem += "\n" + check_tv["text"]
rotulo1["text"] = mensagem
mensagem = "Seus Pertences:"

# estilizando a janela
fonte = ("Arial", "12") #fonte da janela
window = Tk()
window.title("Pesquisa") #titulo da janela
window.geometry("400x200")  #tamanho da janela

#declarando as variaveis como Booleanas
tv = BooleanVar()
pc = BooleanVar()
vg = BooleanVar()
bk = BooleanVar()

#colocando os containers
container1 = Frame(window)
container2 = Frame(window)

container1.pack(side=LEFT)
container2.pack(side=TOP)

#colocando as caixas de botoes

check_tv = Checkbutton(container1, text="televisao", font=fonte, variable=tv, 
                       width=15, anchor="w", padx=10, pady=5, command=verifica_pertences)
check_tv.grid(row=0, column=0)

check_pc = Checkbutton(container1, text="notebook", font=fonte, variable=pc, 
                       width=15, anchor="w", padx=10, pady=5, command=verifica_pertences)
check_pc.grid(row=1, column=0)

check_vg = Checkbutton(container1, text="video-game", font=fonte, variable=vg, 
                       width=15, anchor="w", padx=10, pady=5, command=verifica_pertences)
check_vg.grid(row=2, column=0)

check_bk = Checkbutton(container1, text="bicicleta", font=fonte, variable=tv, 
                       width=15, anchor="w", padx=10, pady=5, command=verifica_pertences)
check_bk.grid(row=3, column=0)

rotulo1 = Label(container2, text="Seus Pertences:" pady=20)
rotulo1["font"] = ("Arial", "14", "bold")
rotulo1.grid(row=0, column=1)

window.mainloop()
