
respuesta = False
while respuesta==False:
    b = float(input("Raiz Cuadrada de = "))
    a = float(b**(1/2))
    print()
    print("Resultado de la Raiz de",b,"=",round(a,2))
    print()
    pregunta = input("¿Deseas sacar una raiz a otro numero?, y/n: ")
    if pregunta == "n":
        respuesta = True
print()