''''

Devemoso agora verificar as operações com o Array,
Temos 3 tipos de operação.

Array com Array
Array com Escalar 
Funções universais dos Arrays

'''
'''
Arrays com Arrays
'''
import numpy as np
#---------------------------------------

arr = np.arange(25).reshape((5,5))
print(arr)
print("-------------------------------------------")
#Soma
arr1 = np.copy(arr+arr)
print(arr1)
print("-------------------------------------------")
#Multiplicação
arr2 = np.copy(arr*arr)
print(arr2)
print("-------------------------------------------")
#Divisão
arr3 = np.copy(arr/arr)
print(arr3)
print("-------------------------------------------")
#Subtração
arr4 = np.copy(arr-arr)
print(arr4)
print("-------------------------------------------")
#Exponenciação
arr5 = np.copy(arr**arr)
print(arr5)
print("-------------------------------------------")

'''
Arrays com Escalar
'''

arr6 = np.copy(arr+5)
print(arr6)
print("-------------------------------------------")
#Multiplicação
arr7 = np.copy(arr*5)
print(arr7)
print("-------------------------------------------")
#Divisão
arr8 = np.copy(arr/5)
print(arr8)
print("-------------------------------------------")
#Subtração
arr9 = np.copy(arr-5)
print(arr9)
print("-------------------------------------------")
#Exponenciação
arr10 = np.copy(arr**5)
print(arr10)
print("-------------------------------------------")


'''
As funções do proprio array podem ser identificada no site, e são aplicadas em cada um dos elementos do Array. São algumas delas
.sqrt() ; .exp() ; .max() ; .min() ; .sin() ; .log() ; .cos()
'''