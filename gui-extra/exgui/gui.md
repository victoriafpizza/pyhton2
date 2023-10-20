MODULO TINKER

O tkinter é uma das ferramentas que o Python oferece para desenvolvimento de interfaces
gráficas. A grande vantagem de utilizar deste módulo é de que ele faz parte do pacote básico
do Python para Windows Saiba que o Idle Python foi desenvolvido pelo módulo tkinter
Veremos alguns termos jocos no desenvolvimento de interfaces gráficas, como:

WIDGET: usado para se referir a um componente qualquer da ui
EVENT HANDLERS: são procedimentos programadaos para serem executados quando um evento acontece
BINDING: é necessário para associar um componente  a algum evento handler

Sempre que trabalharmos com tinker, importaremos todo o conteudo deste modulo.
A classe Tk também é importada, e é dela que conseguimos tirar os widgets com os quais 
montaremos nossa GUI

ex:

from tkinter import *
window = TK()
window.title("Titulo da Janela")
window.mainloop()

X E Y 

Podemos especificar o tamanho de nossa janela com a função geometry() passando 
pixels (separando por x) os valores de largura e altura 
Opcionalmente podemos também indicar a posição inicial da janela, passando coordenadas x e y (separando por +) nesta mesma funçaõ

ex:

window.geometry("350x200+400+200)

Widget Label 

Podemos adicionar a nossa janela um widget do tipo Label (rotulo ou etiqueta).

Atribuimos este widget a uma variavel, indicamos a qual a janela ele pertence,
e configuramos seus atributos (todo widget é tratado como um dicionario,
então basta acessar suas chaves e definir novos valores para configurar seus atributos).

A definição dos atributos de um widget pode ser feita na sua instanciação
ou logo depois (utilizando os nomes de atributo). 

Para finalizar devemos escolher um gerenciados de layout (O Python tem 3 
diferentes). Eles servem para posicionar os widgets na nossa janela e torna-las
visiveis. 

WIDGET BUTTON

Podemos adicionar a nossa janela um widget do tipo button. Atribuimos este
widget a uma variavel, indicamos a qual janela ele pertence e configuramos 
seus atributos (todo widget é tratado como um dicionario, então bsata
acessar suas chaves e definir novos valores para configurar seus atributos)

A definição dos atributos de um widget pode ser feita na sua instanciação 
logo depois (utilizando os nomes das chaves de seu atributo)

Para finalizar devemos escolher um gerenciados de layout (o Python possui 3)
Eles servem para posicionar os widgets na nossa janela e tona-los visiveis

WIDGET ENTRY 

Podemos adicionar a nossa janela um widget do tipo Entry. Este widget é 
usado para receber um simples linha de texto digitado pelo usuário (pode 
ser numero, tambem, porem sera tratado como string)

Para receber multiplas linhas de texto utilizamos outro widget

A função .get() perite ler o que foi digitado neste widget. A função focus()
permite que definir um widget receba o foco ao rodar o programa.

Para melhor organizar os componentes vamos criar um Frame() e colocar 
alguns widgets nele. Depois podemos posicionar estes widgets na função pack
() com o parametro side (valores: RIGHT, CENTER, LEFT, TOP, e BOTTOM)
