while True:
    operacao = input('digite uma operação:(+/-/*)')

    if operacao == '+':
        numero1 = int(input('digite o primeiro numero que deseja soma:'))
        numero2 = int(input('digite o segundo numero que deseja somar:'))

        print(f'o resultado da sua operção é:{numero1 + numero2}')
        continue

    if operacao == '-':
        numero1 = int(input('digite o primeiro numero que deseja subtrair:'))
        numero2 = int(input('digite o segundo numero que deseja subtrair:'))

        print(f'o resultado da sua operção é:{numero1 - numero2}')
        continue

    if operacao == '*':
        numero1 = int(input('digite o primeiro numero que deseja multiplicar:'))
        numero2 = int(input('digite o segundo numero que deseja multiplicar:'))

        print(f'o resultado da sua operção é:{numero1 * numero2}')
        continue