# Dado un integer, escribe una función que regrese la suma todos sus
# dígitos. Es decir, para el integer 12345 las suma de sus dígitos es:
# 1+2+3+4+5 = 15
# Definición de la función
# digitsSum(inputInt: integer):
# integer Casos de ejemplo
# ● Con inputInt = “999”, la salida debería ser digitsSum(inputInt ) = 27;
# ● Con inputInt = “9184501”, la salida debería ser digitsSum(inputInt ) = 28;
# ● Con inputInt = “12345”, la salida debería ser digitsSum(inputInt ) = 15;


def digitsSum(input): 
    suma = sum(int(digito) for digito in str(input))
    return suma
