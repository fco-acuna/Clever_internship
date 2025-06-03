from suma_digitos import *
from palindromo import *
from ordenamiento import *


assert digitsSum(999) == 27
assert digitsSum(9184501) == 28
assert digitsSum(12345) == 15

assert isPalindrome("aabaa") == True
assert isPalindrome("abac") == False
assert isPalindrome("salas") == True

assert integerSort([5, -2, 10, 0, 3, -7]) == [-7, -2, 0, 3, 5, 10]
print("Pruebas completadas exitosamente")