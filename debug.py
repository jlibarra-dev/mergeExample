def sumarUno(numero):
    return numero + 1

numero = 5
for i in range(5):
    numero = sumarUno(numero)

numeros = [1,2,3,4,5]
for i in range(len(numeros)):
    numeros[i] = sumarUno(numeros[i])
