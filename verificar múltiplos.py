def verificar_múltiplos(número):
    divisores = [2, 3, 5, 7, 9, 10, 11]
    


    for divisor in divisores:
        if número % divisor == 0:
            print(f"{número} SÍ es múltiplo de {divisor}")
        else:
            print(f"{número} NO es multiplo de {divisor}")



            

try:
    número = int(input("Ingresa un número entero:"))
    verificar_múltiplos(número)
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
