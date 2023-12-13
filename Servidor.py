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
            quartos = self._carregar_dados_quarto()
            if not quartos:
                print("Não há quartos cadastrados.")
                return

            print("\nStatus dos Quartos:")
            for quarto in quartos:
                print(f"Quarto {quarto.get('numero', 'N/A')} - Tipo: {quarto.get('tipo', 'N/A')}, Status: {quarto.get('status', 'N/A')}")
            print()

        except FileNotFoundError:
            print("Erro: Arquivo de quartos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao carregar e mostrar quartos: {e}')

    def reservar_quarto(self):
        try:
            quartos = self._carregar_dados_quarto()
            if not quartos:
                print("Não há quartos cadastrados.")
                return

            self.numero = input('Qual o número do quarto? ')
            print()
            self.paciente = input('Digite o nome do paciente: ')
            print()
            self.data_checkin = input('Qual a data de checkin? ')
            print()
            self.dias_estadia = input('Quantos dias o paciente ficará internado? ')

            quarto = next((q for q in quartos if q.get('numero') == self.numero and q.get('status') == "Disponível"), None)
            if quarto:
                quarto['status'] = "Ocupado"
                quarto['paciente_atual'] = self.paciente
                quarto['data_checkin'] = datetime.strptime(self.data_checkin, "%Y-%m-%d %H:%M:%S")
                quarto['data_checkout'] = (quarto['data_checkin'] + timedelta(days=int(self.dias_estadia))).strftime("%Y-%m-%d %H:%M:%S")
                print(f"Quarto {quarto.get('numero')} reservado para {self.paciente} até {quarto.get('data_checkout')}")
                time.sleep(3)
            else:
                print(f"Quarto {self.numero} não disponível ou não existe.")
                time.sleep(3)

        except FileNotFoundError:
            print("Erro: Arquivo de quartos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f'Erro ao reservar quarto: {e}')

    def desocupar_quarto(self):
        try:
            self.numero = input('Qual o número do quarto que será desocupado? ')
            print()
            quartos = self._carregar_dados_quarto()
            quarto = next((q for q in quartos if q.get('numero') == self.numero and q.get('status') == "Ocupado"), None)
            if quarto:
                quarto['status'] = "Disponível"
                quarto['paciente_atual'] = None
                quarto['data_checkin'] = None
                quarto['data_checkout'] = None
                print(f"Quarto {quarto.get('numero')} desocupado.")
            else:
                print(f"Quarto {self.numero} não ocupado ou não existe.")

        except FileNotFoundError:
            print("Erro: Arquivo de quartos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao desocupar quarto: {e}')

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
