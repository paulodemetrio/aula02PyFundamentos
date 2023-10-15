user = 1
mod = 2
adm = 3

if __name__ == '__main__' :
    valor = int(input('Informe seu código de permissão: '))
    match valor:
        case 1:
            print('User')
        case 2:
            print('Moderator')
        case 3:
            print('Admin')
        case _:
            print('Acesso negado')