frutas = ("maça", "uva", "tomate", "uva", "kiwi")
print(frutas)
print(len(frutas))
print(frutas.count("uva"))
print(frutas[3])
print(type(frutas))
misto = ("alface", 23, True, 7.33)
print(misto)
print(type(misto))

# empacotar e desempacotar

frutas = ("maca", "uva", "tomate")
(a, b, c) = frutas 
print(f"{a}\n{b}\n{c}")
(x, *y)= frutas
print(f"{x}\n{y}")
frutas = ("maca","uva","tomate","uva","kiwi")
(k, *w, z) = frutas 
print(f"{k}\n{w}\n{z}")