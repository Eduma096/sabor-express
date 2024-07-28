#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
def exercicio_1():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    nomes = ['Eduardo','José Aparecido', 'Fátima', 'Raul']
    anos = [1996,2024]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
def exercicio_2():
    numeros = [1,2,3,4,5,6,7,8,9,10]

    for numero in numeros:
        print(numero)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
def exercicio_3():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    somaPar = 0
    somaImpar = 0

    for numero in numeros:
        if numero % 2 == 0:
            somaPar = somaPar + numero
        else:
            somaImpar = somaImpar + numero
    
    print(f'''A soma dos números pares é: {somaPar}.
A soma dos números impares é: {somaImpar}.''')
    
#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

def exercicio_4():

    for i in range(10, 0, -1):
        print(i)

def exercicio_4_1():
    numeros = [1,2,3,4,5,6,7,8,9,10]

    for numero in sorted(numeros, reverse=True):
        print(numero)

def exercicio_4_2():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    tamanho_numeros = len(numeros)
    posicao = tamanho_numeros-1
    for i in range(tamanho_numeros):
        print(numeros[posicao])
        posicao = posicao-1

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
def exercicio_5():
    tabuada = [1,2,3,4,5,6,7,8,9,10]
    numero = int(input('Digite um número para a tabuada de 1 a 10: '))

    for mutiplica_por in tabuada:
        print(f'{numero} X {mutiplica_por} = {numero*mutiplica_por}') 

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
def exercicio6():
    numeros = [10,50,50,False,10,'pipipi popopo',30,45,5]
    soma = 0
    for numero in numeros:
        try:
            soma = soma + numero
        except:
            pass            
    print(soma)

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

def exercicio7():
    numeros = [5,50,5,1,10,90,30,45,5,50,0]
    tamanho_numeros = len(numeros)
    soma = 0
    try:  
        for numero in numeros:
            try:
                soma = soma + numero
            except:
                pass                      
        media = soma/tamanho_numeros
    except:
        print('Houve uma erro inesperado ou a lista está vazia.')
    print(f'''A soma é {soma}
e a media é {media}''')

#--------------------------------------------------

def main():
    #exercicio_1()
    #exercicio_2()
    #exercicio_3()
    #exercicio_4()
    #exercicio4_1()
    #exercicio_4_2()
    #exercicio_5()
    #exercicio6()
    exercicio7()

if __name__ == '__main__':
    main()
