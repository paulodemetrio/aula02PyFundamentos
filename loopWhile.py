from random import randint

if __name__ == '__main__':
    i = 0
    while i < 10 :
        print(i)
        i += 1
    print(i)

    lista_numeros = []

    while True:
        n = randint(-5, 20) #Retorna um número aleatório entre os dois números dentro dos parêntesis
        if n < 0 :
            print(f'Foi gerado um número negativo: {n}')
            break
        lista_numeros.append(n)
    print(f'Soma: {sum(lista_numeros)}')

    lista_tipos = [2, 4, 5.5, 6.6, 'Python', 'Java', [1, 2, 3], ['a', 'b', 'c']]
    lista_numeros.clear()
    contador = 0
    while contador < len(lista_tipos):
        valor_atual = lista_tipos[contador]
        if not isinstance(valor_atual, int) and not isinstance(valor_atual, float):
            print(f'O valor {valor_atual} não é do tipo numérico.')
            contador += 1
            continue
        lista_numeros.append(valor_atual)
        contador += 1