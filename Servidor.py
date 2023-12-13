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
    QUARTO_FILE = "quartos.txt"
    MEDICAMENTOS_FILE = "medicamentos.txt"
    ESCALA_FILE = "escala_funcionarios.txt"

    def __init__(self):
        self.nome = ''
        self.email = ''
        self.senha = ''
        self.funcao = ''

    def _carregar_dados(self, file):
        if pathlib.Path(file).exists():
            with open(file, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _salvar_dados(self, file, dados):
        with open(file, "w") as arquivo:
            for usuario in dados:
                json.dump(usuario, arquivo)
                arquivo.write('\n')

    def _carregar_dados_escala(self):
        return self._carregar_dados(self.ESCALA_FILE)

    def _carregar_dados_medicamento(self):
        return self._carregar_dados(self.MEDICAMENTOS_FILE)

    def _carregar_dados_quarto(self):
        return self._carregar_dados(self.QUARTO_FILE)

    def _carregar_dados_med(self):
        return self._carregar_dados(self.MEDICO_FILE)

    def _carregar_dados_user(self):
        return self._carregar_dados(self.CLIENTES_FILE)

    def _carregar_dados_serve(self):
        return self._carregar_dados(self.SERVIDOR_FILE)

    def _salvar_dados_serve(self, dados):
        self._salvar_dados(self.SERVIDOR_FILE, dados)

    def _salvar_dados_med(self, dados):
        self._salvar_dados(self.MEDICO_FILE, dados)

    def _salvar_dados_user(self, dados):
        self._salvar_dados(self.CLIENTES_FILE, dados)

    def _salvar_dados_quarto(self, dados):
        self._salvar_dados(self.QUARTO_FILE, dados)

    def _salvar_dados_escala(self, dados):
        self._salvar_dados(self.ESCALA_FILE, dados)

    def _salvar_dados_medicamento(self, dados):
        self._salvar_dados(self.MEDICAMENTOS_FILE, dados)

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
        try:
            dados_quarto = self._carregar_dados_quarto()

            if not dados_quarto:
                print("Não há quartos reservados no momento.")
                return

            print("\nQuartos Reservados:")
            for quarto in dados_quarto:
                print(f"Número do Quarto: {quarto.get('Numero')}")
                print(f"Paciente: {quarto.get('Paciente', 'N/A')}")
                print(f"Data de Check-in: {quarto.get('Data_checkin')}")
                print(f"Dias de Estadia: {quarto.get('Dias estadia')}")
                print("------------------------------")

        except FileNotFoundError:
            print("Erro: Arquivo de quartos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao mostrar quartos: {e}')

    def reservar_quarto(self):
        try:
            self.numero = input('Qual o número do quarto? ')
            print()
            self.paciente = input('Digite o nome do paciente: ')
            print()
            self.data_checkin = input('Qual a data de checkin? ')
            print()
            self.dias_estadia = input('Quantos dias o paciente ficará internado? ')

            dados_quarto = self._carregar_dados_quarto()

            novo_quarto = {
                "Numero": self.numero,
                "Paciente": self.paciente,
                "Data_checkin": self.data_checkin,
                "Dias estadia": self.dias_estadia
            }

            dados_quarto.append(novo_quarto)

            self._salvar_dados_quarto(dados_quarto)

            self._clear_screen()
            print(f'Qaurto reservado para {self.paciente}')
            time.sleep(2)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def desocupar_quarto(self):
        try:
            numero_quarto_desocupar = input('Digite o número do quarto a ser desocupado: ')

            dados_quarto = self._carregar_dados_quarto()

            quarto_encontrado = False

            for quarto in dados_quarto:
                if quarto.get('Numero') == numero_quarto_desocupar:
                    quarto_encontrado = True
                    quarto['Paciente'] = 'N/A'
                    quarto['Data_checkin'] = 'N/A'
                    quarto['Dias estadia'] = 'N/A'
                    break

            if not quarto_encontrado:
                print(f"Quarto {numero_quarto_desocupar} não encontrado.")
            else:
                self._salvar_dados_quarto(dados_quarto)
                print(f'Quarto {numero_quarto_desocupar} desocupado com sucesso.')
                time.sleep(2)

        except Exception as e:
            print(f'Erro ao desocupar o quarto: {e}')
        

    def adicionar_medicamento(self):
        try:
            self.nome = input('Digite o nome do medicamento: ')
            print()
            self.quantidade = input(f'Digite a quantidade de {self.nome} que será adicionada ao estoque: ')
            self.descricao = input('Adicione uma descrição para o medicamento: ')
            medicamentos = self._carregar_dados_medicamento()
            novo_medicamento = {
                "nome": self.nome,
                "quantidade": self.quantidade,
                "descricao": self.descricao
            }
            medicamentos.append(novo_medicamento)
            self._salvar_dados_medicamento(medicamentos)
            print(f"\nMedicamento {self.nome} adicionado ao estoque.\n")

        except FileNotFoundError:
            print("Erro: Arquivo de medicamentos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao adicionar medicamento: {e}')

    def mostrar_medicamentos(self):
        try:
            medicamentos = self._carregar_dados_medicamento()
            if not medicamentos:
                print("Não há medicamentos cadastrados.")
                return

            print("\nEstoque de Medicamentos:")
            for medicamento in medicamentos:
                print(f"{medicamento.get('nome', 'N/A')} - Quantidade: {medicamento.get('quantidade', 'N/A')}, Descrição: {medicamento.get('descricao', 'N/A')}")
            print()

        except FileNotFoundError:
            print("Erro: Arquivo de medicamentos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao mostrar medicamentos: {e}')

    def adicionar_escala(self):
        try:
            self.funcionario =  input('Digite o nome do funcionario que será adicionado a escala: ')
            print()
            self.dias_trabalhados = input(f'Dias da semana que {self.funcionario} irá trabalhar, no seguinte formato:["dias da semana",..]')
            print()
            self.horas_por_dia = input(f'Digite quantas horas {self.funcionario} irá trabalhar por dia')
            escala = self._carregar_dados_escala()
            nova_entrada = {
                "funcionario": self.funcionario,
                "dias_trabalhados": self.dias_trabalhados,
                "horas_por_dia": self.horas_por_dia
            }
            escala.append(nova_entrada)
            self._salvar_dados_escala(escala)
            print(f"\nEscala adicionada para {self.funcionario}.\n")

        except FileNotFoundError:
            print("Erro: Arquivo de escalas não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao adicionar escala: {e}')

    def mostrar_escala(self):
        try:
            escala = self._carregar_dados_escala()
            if not escala:
                print("Não há escalas cadastradas.")
                return

            print("\nEscala de Funcionários:")
            for entrada in escala:
                print(f"Funcionário: {entrada.get('funcionario', 'N/A')}, Dias Trabalhados: {entrada.get('dias_trabalhados', 'N/A')}, Horas por Dia: {entrada.get('horas_por_dia', 'N/A')}")
            print()

        except FileNotFoundError:
            print("Erro: Arquivo de escalas não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao mostrar escala: {e}')
    
    def _hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')




