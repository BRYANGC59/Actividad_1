def factorial ():
    numero = int(input("Ingresar numero:"))
    factorial = 1
    for i in range (numero):
        
        factorial *= i + 1
    print (factorial)

factorial ()
