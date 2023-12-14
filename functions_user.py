from Usuario import Usuario
import os
usuario1 = Usuario()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_user():
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

                                 --------------------
                                | 1 - Cadastre-se    |
                                | 2 - Fazer Login    |
                                | 3 - Voltar         |                
                                ----------------------
        

        """
        ascii_art_lower = ascii_art.lower()

        
        print(ascii_art_lower)                

        escolha = input()
        
        clear_screen()  # Limpa a tela 

        if escolha == '1':
            cadastro = usuario1.cadastro_user()
            if cadastro:
                menu_user()

        elif escolha == '2':
            cliente =  usuario1.login_user()
            if cliente:
                menu_user()
        else:
            return    

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

                     _____________________________________________________________
                    /                                                              \\
                    |                    Escolha uma opção                          |
                    |                                                               |
                    |   1 - Marcar Consulta          5 - Ver exames solicitados /   |
                    |   2 - Remarcar Consulta        Marcar exame                   |
                    |   3 - Desmarcar Consulta       6 - Ver Resultado do Exame     |
                    |   4 - Adicionar Dinheiro       7 - Voltar                     |
                     \_____________________________________________________________/
    
        

        """
        ascii_art_lower = ascii_art.lower()

        
        print(ascii_art_lower)                

        escolha = input()

       
        if escolha == '1':
            clear_screen()
            usuario1.marcar_consulta()

        elif escolha == '2':
            clear_screen()
            usuario1.remarcar_consulta()

        elif escolha == '3':
            clear_screen()
            usuario1.desmarcar_consulta()

        elif escolha == '4':
            clear_screen()
            usuario1.adiocionar_dinheiro()

        elif escolha == '5':
            clear_screen()
            usuario1.print_exames_solicitados_e_marcar_exame()
        
        elif escolha == '6':
            clear_screen()
            email = input('Digite seu email')
            usuario1.print_resultados_exames(email)
         
        else:
            break
