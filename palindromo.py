# Dado un string, escribe una función para verificar si es un palíndromo. Un palíndromo es
# un texto que se lee igual de izquierda a derecha que de derecha a izquierda. Las
# palabras: salas, oso, reconocer y oro son palíndromos.
# Definición de la función
# isPalindrome(inputStr: string):
# boolean Casos de ejemplo
# ● Con inputStr = “aabaa”, la salida debería ser isPalindrome(inputStr) = true;
# ● Con inputStr = “abac”, la salida debería ser isPalindrome(inputStr) = false;
# ● Con inputStr = “salas”, la salida debería ser isPalindrome(inputStr) = true;

def isPalindrome(inputStr):
    if inputStr == inputStr[::-1]:
        return True
    else:
        return False


assert isPalindrome("aabaa") == True
assert isPalindrome("abac") == False
assert isPalindrome("salas") == True
print("Pruebas completadas exitosamente")
