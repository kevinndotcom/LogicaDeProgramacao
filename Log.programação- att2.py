print(' escolha a fruta que você deseja comprar?')
print('banana 1')
print('maça 2')
print('uva 3')
produto = int(input('qual você deseja?'))
qtd = int(input('quantas você deseja?'))
if(produto == 1 ):
    pagar = qtd * 2.50
    print(' você comprou {} bananas e ficou no valor de  {}R$ '.format( qtd, pagar ))
elif(produto == 2):
    pagar = qtd * 1.50
    print('você comprou {} maça e ficou no valor de {}R$'.format(qtd,pagar) )
elif(produto == 3):
    pagar = qtd* 4.50
    print('você comprou {} uvas e ficou no valor de {} R$'.format(qtd,pagar))
else:
    print('este produto não está na lista')