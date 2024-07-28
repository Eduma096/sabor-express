#Interpolação de String
print('\nSabor Express\n')
print('''nSabor Express\n''')
print('''
A
L
U
R
A
''')

nome = 'Eduardo Machado'
idade = 28
print(f'\nMeu nome é {nome} e tenho {idade} anos')

#-------------------------------------------------------

#CONDIÇÕES
#If, else if e else
opcao_escolhida_if = int(input('Escolha uma opção: '))
if opcao_escolhida_if == 1:
    print('Adicionar restaurante')
elif opcao_escolhida_if == 2:
    print('Listar restaurantes')
elif opcao_escolhida_if == 3:
    print('Ativar restaurante')
elif opcao_escolhida_if == 4:
    print('Finalizar app')
else:
    print('Opção inválida!')

#Match
opcao_escolhida_match = int(input('Escolha uma opção: '))
if opcao_escolhida_match == 1:
    print('Adicionar restaurante')
elif opcao_escolhida_match == 2:
    print('Listar restaurantes')
elif opcao_escolhida_match == 3:
    print('Ativar restaurante')
elif opcao_escolhida_match == 4:
    print('Finalizar app')
else:
    print('Opção inválida!')

#-------------------------------------------------------

#Conversões de tipo de variável
#str para int
opcao_escolhida_str = input('Escolha uma opção: ')
opcao_escolhida_int = int(input('Escolha uma opção: '))
print(f'''Opção escolida string: {opcao_escolhida_str}
Opção escolhida Int: {opcao_escolhida_int}''')
