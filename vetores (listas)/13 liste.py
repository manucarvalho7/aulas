lista = []

while True:
    additem = input('adicione um item: ')
    if additem == 'fim':
        break

    lista.append(additem)

print(f'o tamanho da minha lista é: {len(lista)}')
