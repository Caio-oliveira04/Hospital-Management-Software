from Usuario import Usuario
import os
usuario1 = Usuario()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
                

while True:
                                      
    ascii_art = """
 _   _                  _  _       _    _   __
| | | | ___  ___ _ __  (_)| |_ ___| |  | \ /  | __ _ _ ___  ___ _  ___ _
| |_| |/ _ \/ __| '_ \  _  __/ _' | |  |      |/ _' | '   \/ _ ' |/ _ ' |
|  _  | (_) \__ \ |_) || | || (_| | |  |  \/  | (_) |  _  | (_)  | (_|  |
|_| |_|\___/\___/ .__/ |_|\__\__,_|_|  |_|  |_|\__,_|_| |_|\___,_|\___, |
                |_|                                                 __/ |
                                                                   |___/

                          _____________________________________
                        /                                      \\
                        |1 - C a d a s t r e - s e              | 
                        |2 - F a z e r   L o g i n              |
                        |3 - M a r c a r  c o n s u l t a       |
                        |4 - R e m a r c a r  c o n s u l t a   |
                        |5 - D e s m a r c a r  c o n su l t a  |
                        |6 - A d i c i o n a r  d i n h e i r o |
                        |7 - Sair                               |
                        \_______________________________________/    
    

    """

    # Convert ASCII art to lowercase
    ascii_art_lower = ascii_art.lower()

    # Print the lowercase ASCII art
    print(ascii_art_lower)                

    escolha = input('Digite a opção desejada: ')

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
        usuario1.desmarcar_consulta

    elif escolha == '6':
        usuario1.adiocionar_dinheiro()
    else:
        break
