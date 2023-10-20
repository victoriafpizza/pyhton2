#Label

# Podemos utilizar o widget  do tipo label para exibir imagens na janela
# Para isso, primeiramente, podemos atribuir a uma variavel um objeto da classe PhotoImage indicando no parametro file 
# o local e o nome do arquivo da imagem

from tkinter import *

window = Tk()
window.title("Imagem na Janela")
imagem = PhotoImage(file="/img/batman.png")
rotulo = Label(window, image=imagem)
rotulo.pack()

window.mainloop()
