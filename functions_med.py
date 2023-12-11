from Medico import Medico
import os
medico1 = Medico()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
                

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

                     _________________________________________
                    /                                          \\
                    |    Escolha uma opção                      |
                    |                                           |
                    |  1 - Fazer Loguin                         |
                    |  2 - Atender paciente / ver prontuario    |
                    |  3 - Prescrever rémedio                   |
                    |  4 - Solicitar exame                      |
                    \__________________________________________/
  
    

    """

    # Convert ASCII art to lowercase
    ascii_art_lower = ascii_art.lower()

    # Print the lowercase ASCII art
    print(ascii_art_lower)                

    escolha = input()

    clear_screen()  # Limpa a tela após o usuário fazer uma escolha

    if escolha == '1':
        medico1.login_med()

    elif escolha == '2':
        medico1.consulta()

    elif escolha == '4':
        medico1.solicitar_exame("Hemograma")

    elif escolha == '3':
        usuario1.marcar_consulta()

    elif escolha == '4':
        usuario1.remarcar_consulta()

    elif escolha == '5':
        usuario1.desmarcar_consulta()

    elif escolha == '6':
        usuario1.adiocionar_dinheiro()
    else:
        break
