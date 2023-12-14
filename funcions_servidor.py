from Servidor import Servidor
import os
servidor1 = Servidor()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_serv():
    
    login =servidor1._login_servidor()
    if login:
        menu_server()

def menu_server():
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

             ______________________________________________________________________________
            /                                                                               \\
            |                    Escolha uma opção                                           |
            |                                                                                |
            | 1 - Cadastrar medicos                    6 - Adicionar medicamento ao estoque  |
            | 2 - Cadastrar servidores                 7 - Ver estoque                       |
            | 3 - Alocar leito                         8 - Adicionar funcionarios a escala   |
            | 4 - Mostrar ocupação dos leitos          9 - Mostrar a escala                  |
            | 5 - Desalocar leito                      10 - Voltar                           |
            \_______________________________________________________________________________/



        """
        ascii_art_lower = ascii_art.lower()

        
        print(ascii_art_lower)                

        escolha = input()

        clear_screen()  # Limpa a tela 

        if escolha == '1':
            servidor1.cadastro_medico()
        
        elif escolha == '2':
            clear_screen()
            servidor1.cadastro_servidor()

        elif escolha == '3':
            clear_screen()
            servidor1.reservar_quarto()

        elif escolha == '4':
            clear_screen()
            servidor1.mostrar_quartos()
       
        elif escolha == '5':
            clear_screen()
            servidor1.desocupar_quarto()

        elif escolha == '6':
            clear_screen()
            servidor1.adicionar_medicamento()

        elif escolha == '7':
            clear_screen()
            servidor1.mostrar_medicamentos()
        
        elif escolha == '8':
           clear_screen()
           servidor1.adicionar_escala()

        elif escolha == '9':
            clear_screen()
            servidor1.mostrar_escala()    
        
        else:
            break
