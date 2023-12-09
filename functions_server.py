
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
                
medico1 = medico1
servidor1 = Servidor


while True:
                                      
    ascii_art = """
                        _  _       _    _   __
 _   _  ___  ___ _ __  (_)| |_ ___| |  | \ /  | __ _ _ ___  ___ _  ___ _
| |_| |/ _ \/ __| '_ \  _  __/ _' | |  |      |/ _' | '   \/ _ ' |/ _ ' |
|  _  | (_) \__ \ |_) || | || (_| | |  |  \/  | (_) |  _  | (_)  | (_|  |
|_| |_|\___/\___/ .__/ |_|\__\__,_|_|  |_|  |_|\__,_|_| |_|\___,_|\___, |
                |_|                                                 __/ |
                                                                   |___/
           
            1 - médico
            
            2 Adiministração 
    """
    ascii_art_lower = ascii_art.lower()
    print(ascii_art_lower)                

    escolha = input('Quem é você? ') 

    if escolha == '1':
        medico1.menu_med()
    elif escolha == '2':
        servidor1.menu_serv()
        
