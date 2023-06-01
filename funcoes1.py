Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
numeros = [7, 8, 2, 5, 4]
numeros
[7, 8, 2, 5, 4]
numeros[0]
7
numeros[1]
8
len(numeros)
5
numeros[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    numeros[5]
IndexError: list index out of range
for i in range(0, len(numeros)-1):
    for j in range(0, len(numeros)-1 -i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            print(numeros)

            
[7, 2, 8, 5, 4]
[7, 2, 5, 8, 4]
[7, 2, 5, 4, 8]
[2, 7, 5, 4, 8]
[2, 5, 7, 4, 8]
[2, 5, 4, 7, 8]
[2, 4, 5, 7, 8]
def bubble_sort(numeros):
    for i in range(0, len(numeros)-1):
    for j in range(0, len(numeros)-1 -i):
        if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            print(numeros)
            
SyntaxError: expected an indented block after 'for' statement on line 2
def bubble_sort(numeros):
...     for i in range(0, len(numeros)-1):
...         for j in range(0, len(numeros)-1 -i):
...             if numeros[j] > numeros[j + 1]:
...                     numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
...                 print(numeros)
...                 
SyntaxError: unindent does not match any outer indentation level
>>> def bubble_sort(numeros):
...     for i in range(0, len(numeros)-1):
...         for j in range(0, len(numeros)-1 -i):
...             if numeros[j] > numeros[j + 1]:
...                 numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
...                 print(numeros)
... 
...                 
>>> lista = [3, 4, 5, 6, 7, 8, 1, 2, 9, 10, 11, 23, 45, 67, 89, 12]
>>> bubble_sort(lista)
[3, 4, 5, 6, 7, 1, 8, 2, 9, 10, 11, 23, 45, 67, 89, 12]
[3, 4, 5, 6, 7, 1, 2, 8, 9, 10, 11, 23, 45, 67, 89, 12]
[3, 4, 5, 6, 7, 1, 2, 8, 9, 10, 11, 23, 45, 67, 12, 89]
[3, 4, 5, 6, 1, 7, 2, 8, 9, 10, 11, 23, 45, 67, 12, 89]
[3, 4, 5, 6, 1, 2, 7, 8, 9, 10, 11, 23, 45, 67, 12, 89]
[3, 4, 5, 6, 1, 2, 7, 8, 9, 10, 11, 23, 45, 12, 67, 89]
[3, 4, 5, 1, 6, 2, 7, 8, 9, 10, 11, 23, 45, 12, 67, 89]
[3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 11, 23, 45, 12, 67, 89]
[3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 11, 23, 12, 45, 67, 89]
[3, 4, 1, 5, 2, 6, 7, 8, 9, 10, 11, 23, 12, 45, 67, 89]
[3, 4, 1, 2, 5, 6, 7, 8, 9, 10, 11, 23, 12, 45, 67, 89]
[3, 4, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 67, 89]
[3, 1, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 67, 89]
[3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 67, 89]
[1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 67, 89]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 67, 89]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 67, 89]
>>> pessoas = ['Zilma', 'Pedro', 'Ana', 'Júlia', 'Francisco', 'Paulo']
>>> x = -45
>>> abs(x)
45
