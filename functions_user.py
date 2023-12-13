from Usuario import Usuario
import os
usuario1 = Usuario()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
                
def menu_user():
    while True:   

        clear_screen()           
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
                    | 1 - Cadastrar-se               6 - Ver exames solicitados / |
                    | 2 - Fazer Login                Marcar exame                 |
                    | 3 - Marcar Consulta            7 - Ver Resultado do Exame   |
                    | 4 - Remarcar Consulta          8 - Adicionar Dinheiro       |
                    | 5 - Desmarcar Consulta         9 - Voltar                   |
                    \____________________________________________________________/
    
        

        """
        ascii_art_lower = ascii_art.lower()

        
        print(ascii_art_lower)                

        escolha = input()

        clear_screen()  # Limpa a tela 

        if escolha == '1':
            usuario1.cadastro_user()

        elif escolha == '2':
            usuario1.login_user()

        elif escolha == '3':
            usuario1.marcar_consulta()

        elif escolha == '4':
            usuario1.remarcar_consulta()

        elif escolha == '5':
            usuario1.desmarcar_consulta()

        elif escolha == '6':
            usuario1.print_exames_solicitados_e_marcar_exame()
        
        elif escolha == '7':
            email = input('Digite seu email')
            usuario1.print_resultados_exames(email)
        
        elif escolha == '8':
            usuario1.adiocionar_dinheiro()        
        else:
            break
