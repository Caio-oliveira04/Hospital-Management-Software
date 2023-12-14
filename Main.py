from functions_user import login_user
from functions_med import login_med
from funcions_servidor import login_serv

import os
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

                  ____________________________________
                 /                                     \\
                |             Quem é você?              |
                |             1 - Usuario               |
                |             2 - Médico                |
                |             3 - Servidor              |                                                                                        |
                \_______________________________________/
  
    

    """

    # Convert ASCII art to lowercase
    ascii_art_lower = ascii_art.lower()

    # Print the lowercase ASCII art
    print(ascii_art_lower)                

    escolha = input()

    clear_screen()  # Limpa a tela após o usuário fazer uma escolha

    if escolha == '1':
        login_user() 

    elif escolha == '2':
        login_med()

    elif escolha == '3':
        login_serv()
