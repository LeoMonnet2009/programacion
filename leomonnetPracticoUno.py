numeros = [] 
for i in range(10): 
    numero =int(input("Ingrese un numero: ")) 
    numpar = numero % 2
    if numpar== 0: 
        numeros.append(numero)
print(numeros)