from functions_med import menu_med
from functions_user import menu_user
from funcions_servidor import menu_server

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
                |             2 - Medico                |
                |             3 - servidor              |                                                                                        |
                \_______________________________________/
  
    

    """

    # Convert ASCII art to lowercase
    ascii_art_lower = ascii_art.lower()

    # Print the lowercase ASCII art
    print(ascii_art_lower)                

    escolha = input()

    clear_screen()  # Limpa a tela após o usuário fazer uma escolha

    if escolha == '1':
        menu_user()

    elif escolha == '2':
        menu_med()

    elif escolha == '3':
        menu_server()