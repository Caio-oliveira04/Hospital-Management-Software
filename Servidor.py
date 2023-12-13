import json
import os
import pathlib
import time
import hashlib
from datetime import datetime, timedelta
from Usuario import Usuario

class Servidor:
    CLIENTES_FILE = "clientes.txt"
    MEDICO_FILE = "medicos.txt"
    SERVIDOR_FILE = "servidor.txt"
    QUARTOS_FILE = "quartos.txt"
    MEDICAMENTOS_FILE = "medicamentos.txt"
    ESCALA_FILE = "escala_funcionarios.txt"

    def __init__(self):
        self.nome = ''
        self.email = ''
        self.senha = ''
        self.funcao = ''

    def cadastro_medico(self):
        try:
            self.nome = input('Digite o nome do Médico: ')
            self.email = input('Digite o email do mesmo: ')
            self.senha = input('Digite a senha: ')
            self.crm = input('Digite o CRM: ')
            self.especialidade = input('Digite a especialidade: ')

            dados_med = self._carregar_dados_med()

            novo_med = {
                "Nome": self.nome,
                "Email": self.email,
                "Senha": self._hash_senha(self.senha),
                "Crm": self.crm,
                "Especialidade": self.especialidade,
            }

            dados_med.append(novo_med)

            self._salvar_dados_med(dados_med)

            self._clear_screen()
            print('Cadastro feito com sucesso')
            time.sleep(2)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def cadastro_servidor(self):
        try:
            self.nome = input('Digite o nome: ')
            self.email = input('Digite o email do mesmo: ')
            self.senha = input('Digite a senha: ')
            self.funcao = input('Digite a função do servidor: ')

            dados_servidor = self._carregar_dados_serve()

            novo_servidor = {
                "Nome": self.nome,
                "Email": self.email,
                "Senha": self._hash_senha(self.senha),
                "Função": self.funcao
            }

            dados_servidor.append(novo_servidor)

            self._salvar_dados_serve(dados_servidor)

            self._clear_screen()
            print('Cadastro feito com sucesso')
            time.sleep(2)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def mostrar_quartos(self):
        
        quartos = self._carregar_quartos()
        print("\nStatus dos Quartos:")
        for quarto in quartos:
            print(f"Quarto {quarto['numero']} - Tipo: {quarto['tipo']}, Status: {quarto['status']}")
        print()

    def reservar_quarto(self):
        self.numero = input('Qual o número do quarto? ')
        print()
        self.paciente = input('Digite o nome do paciente: ')
        print()
        self.data_checkin = input('Qual a data de checkin? ')
        print()
        self.dias_estadia = input('Quantos dias o paciente ficará internado? ')
        quartos = self._carregar_quartos()
        quarto = next((q for q in quartos if q['numero'] == self.numero and q['status'] == "Disponível"), None)
        if quarto:
            quarto['status'] = "Ocupado"
            quarto['paciente_atual'] = self.paciente
            quarto['data_checkin'] = self.data_checkin.strftime("%Y-%m-%d %H:%M:%S")
            quarto['data_checkout'] = (self.data_checkin + timedelta(days=self.dias_estadia)).strftime("%Y-%m-%d %H:%M:%S")
            print(f"Quarto {quarto['numero']} reservado para {self.paciente} até {quarto['data_checkout']}")
            time.sleep(3)
        else:
            print(f"Quarto {self.numero} não disponível ou não existe.")
            time.sleep(3)
    def desocupar_quarto(self):
        self.numero = input('Qual o número do quarto que será desocupado? ')
        print()
        quartos = self._carregar_quartos()
        quarto = next((q for q in quartos if q['numero'] == self.numero and q['status'] == "Ocupado"), None)
        if quarto:
            quarto['status'] = "Disponível"
            quarto['paciente_atual'] = None
            quarto['data_checkin'] = None
            quarto['data_checkout'] = None
            print(f"Quarto {quarto['numero']} desocupado.")
        else:
            print(f"Quarto {self.numero} não ocupado ou não existe.")

    def adicionar_medicamento(self):
        self.nome = input('Digite o nome do medicamento: ')
        print()
        self.quantidade = input(f'Digite a quantidade de {self.nome} que será adicionada ao estoque: ')
        self.descricao = input('Adicione uma descriação para o medicamento: ')
        medicamentos = self._carregar_medicamentos()
        novo_medicamento = {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "descricao": self.descricao
        }
        medicamentos.append(novo_medicamento)
        self._salvar_medicamentos(medicamentos)
        print(f"\nMedicamento {self.nome} adicionado ao estoque.\n")

    def mostrar_medicamentos(self):
        medicamentos = self._carregar_medicamentos()
        print("\nEstoque de Medicamentos:")
        for medicamento in medicamentos:
            print(f"{medicamento['nome']} - Quantidade: {medicamento['quantidade']}, Descrição: {medicamento['descricao']}")
        print()

    def adicionar_escala(self):
        self.funcionario =  input('Digite o nome do funcionario que será adicionado a escala: ')
        print()
        self.dias_trabalhados = input(f'Dias da semana que {self.funcionario} irá trabalhar, no seguinte formato:["dias da semana",..]')
        print()
        self.horas_por_dia = input(f'Digite quantas horas {self.funcionario} irá trabalhar por dia')
        escala = self.carregar_escala()
        nova_entrada = {
            "funcionario": self.funcionario,
            "dias_trabalhados": self.dias_trabalhados,
            "horas_por_dia": self.horas_por_dia
        }
        escala.append(nova_entrada)
        self.salvar_escala(escala)
        print(f"\nEscala adicionada para {self.funcionario}.\n")

    def mostrar_escala(self):
        escala = self.carregar_escala()
        print("\nEscala de Funcionários:")
        for entrada in escala:
            print(f"Funcionário: {entrada['funcionario']}, Dias Trabalhados: {entrada['dias_trabalhados']}, Horas por Dia: {entrada['horas_por_dia']}")
        print()

    def carregar_escala(self):
        if pathlib.Path(self.ESCALA_FILE).exists():
            with open(self.ESCALA_FILE, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def salvar_escala(self, escala):
        with open(self.ESCALA_FILE, "w") as arquivo:
            for entrada in escala:
                json.dump(entrada, arquivo)
                arquivo.write('\n')

    def _carregar_quartos(self):
        if pathlib.Path(self.QUARTOS_FILE).exists():
            with open(self.QUARTOS_FILE, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _salvar_quartos(self, quartos):
        with open(self.QUARTOS_FILE, "w") as arquivo:
            for quarto in quartos:
                json.dump(quarto, arquivo)
                arquivo.write('\n')

    def _carregar_dados_med(self):
        if pathlib.Path(self.MEDICO_FILE).exists():
            with open(self.MEDICO_FILE, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _carregar_dados_user(self):
        if pathlib.Path(self.CLIENTES_FILE).exists():
            with open(self.CLIENTES_FILE, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _carregar_dados_serve(self):
        if pathlib.Path(self.CLIENTES_FILE).exists():
            with open(self.SERVIDOR_FILE, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _salvar_dados_serve(self, dados):
        with open(self.SERVIDOR_FILE, "w") as arquivo:
            for usuario in dados:
                json.dump(usuario, arquivo)
                arquivo.write('\n')

    def _salvar_dados_med(self, dados):
        with open(self.MEDICO_FILE, "w") as arquivo:
            for usuario in dados:
                json.dump(usuario, arquivo)
                arquivo.write('\n')

    def _salvar_dados_user(self, dados):
        with open(self.CLIENTES_FILE, "w") as arquivo:
            for usuario in dados:
                json.dump(usuario, arquivo)
                arquivo.write('\n')

    def _hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def _buscar_usuario_por_email(self, email, dados):
        for i, usuario in enumerate(dados):
            if usuario["Email"] == email:
                return usuario, i

        return None, -1

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
