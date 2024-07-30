#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
def exercicio_1():
    pessoa = {'nome':'Eduardo', 'data_nascimento':'03-01-1996', 'nacionalidade':'Brasileiro'}
    print(f'O {pessoa.get('nome')} nasceu em {pessoa.get('data_nascimento')} e é {pessoa.get('nacionalidade')}')

#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.
def exercicio_2():
    pessoa = {'nome':'Eduardo', 'data_nascimento':'03-01-1996', 'nacionalidade':'Brasileiro'}
    print(f'O {pessoa.get('nome')} nasceu em {pessoa.get('data_nascimento')} e é {pessoa.get('nacionalidade')}')
    
    pessoa.update({'profissao':input('Qual a nova profissão que você deseja para o Eduardo? ')})
    
    print(f'O {pessoa.get('nome')} nasceu em {pessoa.get('data_nascimento')}, é {pessoa.get('nacionalidade')} e é {pessoa.get('profissao')}')
    del pessoa['data_nascimento']
    print(pessoa)

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
def exercicio_3():
    numeros = {1:1**2, 2:2**2, 3:3**2, 4:4**2, 5:5**2}
    print (numeros)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
def exercicio_4():
    existe_chave = {'chave1':'Este é o valor da chave1','chave2': 'Este é o valor da chave2'}
    chave_buscada = input('Digite o nome da chave: ')
    mensagem = (f'A Chave {chave_buscada} não foi encontrada')
    for chave in existe_chave.keys():
        if chave == chave_buscada:
            mensagem = (f'A chave {chave} foi encontrada')
    print(mensagem)

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
def exercicio_5():
    import re
    frase = input('Digite a frase que desejar: ')

    #trata a frase tirando pontuações mas mantendo acentuações e coloca tudo em minúsculo.
    frase = re.sub(r'[^a-zA-Z0-9\sçáéíóúâêîôûãõÁÉÍÓÚÂÊÎÔÛÃÕ]', '', frase)
    frase = frase.lower()

    #separa as palavras e coloca numa lista
    palavras_da_frase = frase.split()
    
    try:
        #Inicializa o dicionário        
        #palavras = {palavras_da_frase[0]:0}
        contagem_palavras = {}
        print('\nAgora vamos ver com que frequência as palavras se repetem.\n')

        #Formata para tabela para visualizar melhor
        print(f'{'Palavra'.ljust(20)}|Quantidade')   

        #Percorre as palavras da frase
        for palavra in palavras_da_frase:
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1    

        #Exibe as palavras e a quantidade de repetição
        for palavra_key in contagem_palavras:
            print(f'{palavra_key.ljust(20)}|{contagem_palavras.get(palavra_key)}')

    except:
        print('Não foi digitada uma frase.')

#1a versao sem saber direito os conceitos do dicionario
def exercicio_5_leigo():
    import re
    frase = input('Digite a frase que desejar: ')

    #trata a frase tirando pontuações mas mantendo acentuações e coloca tudo em minúsculo.
    frase = re.sub(r'[^a-zA-Z0-9\sçáéíóúâêîôûãõÁÉÍÓÚÂÊÎÔÛÃÕ]', '', frase)
    frase = frase.lower()

    #separa as palavras e coloca numa lista
    palavras_da_frase = frase.split()
    
    try:
        #Inicializa o dicionário        
        #palavras = {palavras_da_frase[0]:0}
        contagem_palavras = {palavras_da_frase[0]:0}
        print('\nAgora vamos ver com que frequência as palavras se repetem.\n')

        #Percorre as palavras da frase
        for palavra in palavras_da_frase:

            #variáveis de controle
            adiciona_key = False
            quantidade = 0

            #percorre as chaves do dicionário
            for chave in contagem_palavras.keys():            
                if palavra == chave:
                    quantidade = contagem_palavras.get(palavra)
                    contagem_palavras.update({palavra:quantidade + 1})
                else:
                    adiciona_key = True
            #adiciono uma nova palavra na key e reseto as variáveis de controle
            if adiciona_key:
                contagem_palavras.update({palavra:quantidade+1})
                adiciona_key = False
                quantidade = 0

        #Formata para tabela para visualizar melhor
        print(f'{'Palavra'.ljust(20)}|Quantidade')   

        #Exibe as palavras e a quantidade de repetição
        for palavra_key in contagem_palavras:
            print(f'{palavra_key.ljust(20)}|{contagem_palavras.get(palavra_key)}')

    except:
        print('Não foi digitada uma frase.')
    
def main():
    #exercicio_1()
    #exercicio_2()
    #exercicio_3()
    #exercicio_4()
    exercicio_5()
    #exercicio_5_leigo()

if __name__ == '__main__':
    main()
