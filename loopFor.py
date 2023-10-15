if __name__ == '__main__':
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for numero in lista_numeros:
        print(f'O quadrado de {numero} é {numero*numero}')
    
    tupla_multiplicar = ((3, 4), (4, 7), (5, 2), (8, 3), (9, 5))
    
    for tupla in tupla_multiplicar:
        numero1, numero2 = tupla
        print(f'{numero1} x {numero2} = {numero1*numero2}')

    lista_acertos = [True, True, True, False, True]
    for acerto in lista_acertos:
        if not acerto:
            print('Error')
            break
        else:
            print('Acerto')

    lista_notas = [4.5, 4.7, 3.8, 3.9, 4, 4.6, 4.6, 3.8, 4.1, 4.2]
    nota_abaixo_de_4 = 0
    media = 0
    soma = 0
    for nota in lista_notas:
        if nota<4:
            nota_abaixo_de_4 += 1
            print(f'Nota abaixo de 4: {nota}')
            continue
        soma += nota
        media = soma / len(lista_notas)
    print(f'Média final: {media}')

    lista_linguagens = ['Java', 'Python', 'C++', 'PHP']
    for l in lista_linguagens:
        if l == 'Python':
            print('Python é legal')
            # break
        else:
            print(l)

