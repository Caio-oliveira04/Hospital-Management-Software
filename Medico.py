import json
import pathlib
import os
import time
import hashlib

class Medico:
    
    CLIENTES_FILE = "clientes.txt"

    def __init__(self):
        self.nome = ''
        self.especialidade = ''
        self.crm = ''
        self.hospital_vinculado = ''

    def menu_med():

        dados = self._carregar_dados()
        case = int(input("O que deseja fazer?\n"
                                    "1 - Prescrever Medicamento\n"
                                    "2 - Solicitar Exame \n"
                                    "6 - Voltar para menu de servidores\n"))
        
        if case == 1:
            self.prescrever_medicacao(dados)
        
        elif case == 2:
            solicitar_exame()
        else:
            return

    def prescrever_medicacao(self, dados):
        email = input("Por favor, digite o email do paciente para o qual você irá prescrever: ")
        usuario, index = self._buscar_usuario_por_email(email, dados)
        self.clear_screen()

        decisao = input('Ver remédio que o paciente já está tomando (Sim/Não)?').lower()
        
        while decisao not in ['sim', 'não']:
            print("Por favor, responda com 'Sim' ou 'Não'.")
            decisao = input('Ver remédio que o paciente já está tomando (Sim/Não)?').lower()

        if decisao == 'sim':
            medicamentos_antigos = dados.get("Medicamentos", [])
            print("Medicamentos:")
            for i in medicamentos_antigos:
                print("-", i)

        novo_medicamento = input("Digite o novo medicamento: ")
        usuario["Medicamentos"].append(novo_medicamento)

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')    
