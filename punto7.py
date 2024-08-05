Lista = [5,35,12, 4, 32, 10]

mayor = Lista[0]
menor = Lista[0]

for numero in Lista:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)