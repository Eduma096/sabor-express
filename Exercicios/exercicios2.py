# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def exercicio_1():
    numero = int(input('Digite qualquer número: '))

    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é impar.')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
def exercicio_2():
    idade = int(input('Digite sua idade: '))
    if 0 < idade <= 12:
        print('Criança')
    elif idade >= 13 and idade < 18:
        print('Adolescente')
    elif idade >= 18:
        print('Adulto')
    else: 
        print('Não nasceu ainda.')

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores 
#esperados determinados por você.
def exercicio_3():
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

    if nome == 'duduzinhos2' and senha == '0960':
        print('Valores corretos.')
    else:
        print('Nome de usuário e/ou senha incorretos.')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano
#o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.
def exercicio_4():
    x = float(input('Digite a coordenada X: '))
    y = float(input('Digite a coordenada Y: '))

    if x > 0 and y > 0:
        print('Primeiro Quadrante')
    elif x < 0 and y > 0:
         print('Segundo Quadrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x > 0 and y < 0:
         print('Quarto Quadrante')
    else:
        print('Caso contrário')

def main():
    #exercicio_1()
    #exercicio_2()
    #exercicio_3()
    exercicio_4()

if __name__ == '__main__':
    main()
