from Usuario import Usuario
import os
usuario1 = Usuario()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
                

while True:
                                      
    ascii_art = """
                        _  _       _    _   __                                                      _
 _   _  ___  ___ _ __  (_)| |_ ___| |  | \ /  | __ _ _ ___  ___ _  ___ _  ___ _ __ ___   ___  _ ___| |_
| |_| |/ _ \/ __| '_ \  _  __/ _' | |  |      |/ _' | '   \/ _ ' |/ _ ' |/ _ \ '_ ' _ \ / _ \| '   \ __| 
|  _  | (_) \__ \ |_) || | || (_| | |  |  \/  | (_) |  _  | (_)  | (_|  |   _/ | | | | |   _/|  _  | |_  
|_| |_|\___/\___/ .__/ |_|\__\__,_|_|  |_|  |_|\__,_|_| |_|\___,_|\___, |\___|_| |_| |_|\___||_| |_|\__|
                |_|                                                 __/ | 
                                                                   |___/

                     ___________________________________________________________
                    /                                                            \\
                    |                    Escolha uma opção                        |
                    |                                                             |
                    | 1 - Cadastrar-se               6 - Ver exames solicitados   |
                    | 2 - Fazer Login                7 - Marcar exame             |
                    | 3 - Marcar Consulta            8 - Ver Resultado do Exame   |
                    | 4 - Remarcar Consulta          9 - Adicionar Dinheiro       |
                    | 5 - Desmarcar Consulta         10 - Sair                    |
                    \____________________________________________________________/
  
    

    """

    # Convert ASCII art to lowercase
    ascii_art_lower = ascii_art.lower()

    # Print the lowercase ASCII art
    print(ascii_art_lower)                

    escolha = input()

    clear_screen()  # Limpa a tela após o usuário fazer uma escolha

    if escolha == '1':
        nome = input('Digite seu nome: ')
        email = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        usuario1.set_nome(nome)
        usuario1.set_email(email)
        usuario1.set_senha(senha)
        usuario1.cadastro_user(nome, email, senha)

    elif escolha == '2':
        email = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        usuario1.set_email(email)
        usuario1.set_senha(senha)
        usuario1.login_user(email, senha)

    elif escolha == '3':
        usuario1.marcar_consulta()

    elif escolha == '4':
        usuario1.remarcar_consulta()

    elif escolha == '5':
        usuario1.desmarcar_consulta()

    elif escolha == '6':
        usuario1.print_exames_solicitados()
    else:
        break
