from Servidor import Servidor
import os
servidor1 = Servidor()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
                
def menu_server():
    while True:
                   
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
            | 1 - Cadastrar medicos                      6 - Ver estoque                     |
            | 2 - Alocar leitos                          7 - Adicionar funcionarios a escala |
            | 3 - Mostrar ocupação dos leitos            8 - Mostrar a escala                |
            | 4 - Desalocar leito                        9 - Ver faturamento geral           |
            | 5 - Adicionar medicamento ao estoque       10 - Voltar                         |
            \_______________________________________________________________________________/



        """
        ascii_art_lower = ascii_art.lower()

        
        print(ascii_art_lower)                

        escolha = input()

        clear_screen()  # Limpa a tela 

        if escolha == '1':
            servidor1.cadastro_medico()

        elif escolha == '2':
            servidor1.reservar_quarto()

        elif escolha == '3':
            servidor1.mostrar_quartos()
       
        elif escolha == '4':
            servidor1.desocupar_quarto()

        elif escolha == '5':
            servidor1.adicionar_medicamento()

        elif escolha == '6':
            servidor1.mostrar_medicamentos()
        
        elif escolha == '7':
           servidor1.adicionar_escala()

        elif escolha == '8':
            servidor1.mostrar_escala()        

        elif escolha == '9':
            servidor1.faturamento_geral()
        else:
            break
