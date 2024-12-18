def contar_vocales(frase):
     
  vocales = 'aeiou'
  contador = {vocal: 0 for vocal in vocales}

  for caracter in frase:
    if caracter.lower() in vocales:
      contador[caracter.lower()] += 1

  return contador

frase = input("Ingrese una frase: ")
resultado = contar_vocales(frase)

print("Cantidad de vocales:")
for vocal, cantidad in resultado.items():
  print(f"- {vocal}: {cantidad}")