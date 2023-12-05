from Usuario import Usuario
import os

usuario1 = Usuario()

def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

while(1):

    print('1 - Cadastre-se'   )
    print('2 - Fazer Loguin'   )
    print('3 - Marcar consulta' )
    print('4 - Remarcar consulta')
    print('5 - Desmarcar consulta')
    print('6 - Sair'               )

    escolha = input('Digite a Opção desejada: ')
    
    clear_screen()  # Clear the screen after the user makes a choice

    if escolha == '1':
        nome = input('Digite seu nome: '   )
        email = input('Diggite seu Email: ')
        senha = input('Digite sua senha: ' )
        usuario1.set_nome(nome)
        usuario1.set_email(email)
        usuario1.set_senha(senha)
        usuario1.cadastro_user(nome, email, senha)

    elif escolha == '2':
        email = input('Diggite seu Email: ')
        senha = input('Digite sua senha: ' )
        usuario1.set_email(email)
        usuario1.set_senha(senha)
        usuario1.login_user(email, senha)
    
    elif escolha == '6':
        break

