from tkinter import *

def soma():
    num1 = float(caixa_texto1.get())
    num2 = float(caixa_texto2.get())
    total = num1 + num2
    rotulo["text"] = f"Resultado: {total:.2f}"

window = Tk()
window.title("Calculadora")
window.geometry("600x200+400+200")

# Styling
window.configure(bg="grey")
rotulo = Label(window, text="Digite dois números:", font=("Arial", 14), bg="grey")
rotulo.pack(pady=10)

container = Frame(window, bg="pink")
container.pack()

# The labels and Entry widgets are arranged as requested
caixa_1_label = Label(container, text="Nmr 1: ", font=("Arial", 12), bg="grey")
caixa_1_label.pack(side=LEFT)

caixa_texto1 = Entry(container, font=("Arial", 12))
caixa_texto1.pack(side=LEFT, padx=10)

caixa_2_label = Label(container, text="Nmr 2: ", font=("Arial", 12), bg="grey")
caixa_2_label.pack(side=LEFT)

caixa_texto2 = Entry(container, font=("Arial", 12))
caixa_texto2.pack(side=LEFT, padx=10)

botao = Button(window, text="Somar", pady=5, padx=10, bg="grey", fg="black", font=("Arial", 14), command=soma)
botao.pack(pady=20)

result_label = Label(window, text="", font=("Arial", 16), bg="pink")
result_label.pack()

window.mainloop()