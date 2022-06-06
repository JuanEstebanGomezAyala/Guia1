A = int(input("Ingresa un numero de 4 digitos: "))

c4 = A % 10
c3 = int((A % 100) / 10)
c2 = int((A % 1000) / 100)
c1 = int((A - (A % 1000)) / 1000)

print(str(c4)+str(c3)+str(c2)+str(c1))