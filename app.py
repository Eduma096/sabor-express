import os

#Variáveis
restaurantes = ['Pizza Playstation','Pastel Xbox', 'Sushi Nintendo']

#Definições/Funções
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu.')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def exibir_nome_do_programa():
    print('\nSabor Express\n')
    
def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restanrantes')
    print('3 - Ativar restaurante')
    print('4 - Sair')

def finalizar_app():
    exibir_subtitulo('Programa encerrado.\n')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes\n')
    for restaurante in restaurantes:
        print(f' - {restaurante}')
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
                print('Ativar restaurante')
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
