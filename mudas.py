'''saco=0,05
ponteiro = 0,17
enxerto=0,15'''

print('\033[1m*-*'*10,'\033[1;33mCEARA MUDAS','\033[1m*-*\033[m'*10)
print('')
qtdsaco=int(input('Quantidade de Sacos cheios: '))
qtdponterios=int(input('Quantidade de Ponteiros: '))
qtdenxertodito=int(input('Quantidade de Enxertos Feitos pelo DITO: '))
qtdenxertos=int(input('Quantidade de Enxertos Feitos tercerizado: '))
print('')
vlrsaco=qtdsaco*0.05
vlrponteiros=qtdponterios*0.17
vlrenxertos=qtdenxertos*0.15
totenxerto=qtdenxertodito+qtdenxertos
print('Valores a serem pagos:')
print('Foram enchidos {} sacos, valor devido é R${}'.format(qtdsaco,vlrsaco))
print('Foi retirado {} ponteiros, Valor devido é R${:.2f}.'.format(qtdponterios,vlrponteiros))
print('Foram enxertados {} mudas,{} Dito e {} Tercerizado, valor a ser pago R${}'.format(totenxerto,qtdenxertodito,qtdenxertos,vlrenxertos))

