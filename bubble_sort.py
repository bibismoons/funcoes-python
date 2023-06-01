def bubble_sort(lista):
    for i in range(0, len(lista) -1):
        for j in range(0, len(lista) -1 -i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            #print(lista)
    return lista

while True:
    valor_inicial = input("Digite os elementos da sua lista:")
    valores = eval("["+valor_inicial+"]")
    print(bubble_sort(valores))
