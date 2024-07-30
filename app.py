import os

#Variáveis
#LISTA
#restaurantes = ['Pizza Playstation','Pastel Xbox', 'Sushi Nintendo'] 

#DICIONARIO
restaurantes = [{'nome':'Pizza Mario', 'categoria':'Italiana', 'ativo':False},
                {'nome':'Hamburgueria Xbox', 'categoria':'Estadunidense', 'ativo':True},
                 {'nome':'Sushi Nintendo', 'categoria':'Japonesa', 'ativo':True} ]

#Definições/Funções
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu.')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(f'{linha}\n{texto}\n{linha}\n')

def exibir_nome_do_programa():
    print('\nSabor Express')
    
def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restanrantes')
    print('3 - Alterar status do restaurante')
    print('4 - Sair')

def finalizar_app():
    exibir_subtitulo('Programa encerrado.')

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input('Digite a categoria do restaurante: ')
    restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria_do_restaurante, 'ativo' : False}
    restaurantes.append(restaurante)
    print(f'O restaurante {restaurante['nome']} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')    
    print(f'{'Nome'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alterar_status_restaurante():
    exibir_subtitulo('Alterar status de restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.' 
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
