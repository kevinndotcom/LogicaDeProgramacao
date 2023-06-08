print('Seja bem-vindo! \n'
      'A sorveteria')
print('------------------------------------------------------- CARDÁPIO -------------------------------------------------------')
print('| CÓDIGO |   DES   DESCRIÇÃO     |         TAMANHO P (500 ml)       |    TAMANHO M (1000ml )  |   TAMANHO G (2000ml)   |')
print('|   TR   |     S. Tradicionais   |               R$ 6,00            |        R$ 10,00         |           R$ 18,00     |')
print('|   ES   |     S. Especiais      |               R$ 7,00            |        R$ 12,00         |           R$ 21,00     |')
print('|   PR   |     S. Premium        |               R$ 8,00            |        R$ 14,00         |           R$ 24,00     |')
print('------------------------------------------------------------------------------------------------------------------------')
acumulador = 0 # soma todos os valores do pedido e apresenta o total da compra
while  True:
    tamanho = input('Qual o tamanho que você deseja (P/ M/ G)? ')
    tamanho = tamanho.upper()
    if  tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Opção inválida. Tamanho digitado está incorreto.')
        continue # se o usuário digitar algo inválido volta para o começo do while

    codigo = input('Digite o código do sabor que você deseja: ')
    codigo = codigo.upper()
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('Incorreto. Este código não corresponde com  o sabor do cárdapio ')
        continue # se o usuário digitar algo inválido volta para o começo do while

    if codigo == 'TR' and tamanho == 'P':
        print('você escolheu o sabor tradicional tamanho P')
        acumulador = acumulador +  6.00 # pega o valor que tinha no acumulador e soma com 6.00
        print('-' * 124)
    elif (codigo == 'TR' and tamanho == 'M'):
        print('você escolheu o sabor tradicional tamanho M')
        acumulador  = acumulador+ 10.00 # pega o valor que tinha no acumulador e soma com 10.00
        print('-' * 124)
    elif (codigo == 'TR' and tamanho == 'G'):
        print('você escocumulador + lheu o sabor tradicional tamanho G')
        acumulador = acumulador+ 18.00 # pega o valor que tinha no acumulador e soma com 18.00
        print('-' * 124)
    elif (codigo == 'ES' and tamanho == 'P'):
        print('você escolheu o sabor especial tamanho P')
        acumulador = acumulador+ 7.00 # pega o valor que tinha no acumulador e soma com 7.00
        print('-' * 124)
    elif (codigo == 'ES' and tamanho == 'M'):
        print('você escolheu o sabor especial tamanho M')
        acumulador = acumulador + 12.00 # pega o valor que tinha no acumulador e soma com 12.00
        print('-' * 124)
    elif (codigo == 'ES' and tamanho == 'G'):
        print('você escolheu o sabor especial tamanho G')
        acumulador = acumulador +  21.00 # pega o valor que tinha no acumulador e soma com 21.00
        print('-' * 124)
    elif (codigo == 'PR' and  tamanho =='P'):
        print('você escolheu o sabor premium tamanho P')
        acumulador = acumulador +   8.00 # pega o valor que tinha no acumulador e soma com 8.00
        print('-' * 124)
    elif (codigo == 'PR' and tamanho== 'M'):
        print('você escolheu o sabor premium tamanho M')
        acumulador = acumulador +  14.00  # pega o valor que tinha no acumulador e soma com 14.00
        print('-' * 124)
    elif (codigo == 'PR' and tamanho =='G'):
        print('você escolheu o sabor premium tamanho G')
        acumulador = acumulador +  24.00  # pega o valor que tinha no acumulador e soma com 24.00

    pedir_mais = input('Deseja pedir mais algum sorvete (S/N)? ')
    print('-' * 124)
    pedir_mais = pedir_mais.upper()
    if pedir_mais == 'S':
        continue # volta para o começo do while para fazer os pedidos
        print('-' * 124)
    else:
        print('O valor total a ser pago: R$ {:.2f}'.format(acumulador))
        print('-' * 124)
        break # finaliza o loop e encerra o programa