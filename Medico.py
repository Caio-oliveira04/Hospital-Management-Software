import json
import os
import pathlib
import time
import hashlib
from Usuario import Usuario

class Medico:
    CLIENTES_FILE = "clientes.txt"
    MEDICO_FILE = "medicos.txt"

    def __init__(self):
        self.nome = ''
        self.email = ''
        self.senha = ''
        self.especialidade = ''
        self.crm = ''
        self.hospital_vinculado = ''

    def cadastro_medico(self):
        try:
            self.nome = input('Digite o nome do Médico: ')
            self.email = input('Digite o email: ')
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

            self.clear_screen()
            print('Cadastro feito com sucesso')
            time.sleep(2)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def _login_med(self):
        try:
            dados_med = self._carregar_dados_med()
            self.email = input('Digite o email: ')
            self.senha = input('Digite a senha: ')

            for usuario in dados_med:
                if usuario["Email"] == self.email and usuario["Senha"] == self._hash_senha(self.senha):
                    print("Login feito com sucesso!")
                    time.sleep(2)
                    return True
                elif usuario["Email"] == self.email and usuario["Senha"] != self.senha:
                    print("Senha incorreta")
                    time.sleep(2)
                    return
                elif usuario["Email"] != self.email and usuario["Senha"] == self.senha:
                    print("Email incorreto")
                    time.sleep(2)
                    return

            print("Email não encontrado.")


        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
        except Exception as e:
            print(f'Erro ao realizar login: {e}')

    def consulta(self):
        dados = self._carregar_dados_user()
        email = input("Digite o email do paciente: ")
        usuario, index = self._buscar_usuario_por_email(email, dados)

        if usuario:
            print(f'PRONTUARIO de {usuario["Nome"]}')
            
            usuario2 = Usuario()
            usuario2.print_resultados_exames(email)

            # Pergunte ao médico se deseja marcar um exame
            decisao = input('Deseja marcar um exame para este paciente? (sim/não) ')
            if decisao.lower() == 'sim':
                self.solicitar_exame(email)
        else:
            print(f"Usuário com o email {email} não encontrado.")

    def solicitar_exame(self, email):
        try:
            nome_exame = input('Qual o nome do exame a ser marcado? ')
            dados = self._carregar_dados_user()

            usuario, index = self._buscar_usuario_por_email(email, dados)

            if usuario:
                usuario["Exames_solicitados"].append(nome_exame)
                self._salvar_dados_user(dados)  # Corrigido para salvar dados do usuário
                print(f'Exame "{nome_exame}" solicitado com sucesso!')
                print()
                decisao = input('Deseja marcar mais alguem exame? (Sim/Não)?')
                if decisao.lower() == 'sim':
                    self.solicitar_exame(email)
                else:
                    time.sleep(2)
                    return
            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao solicitar o exame: {e}')

    def receitar_remedio(self):
        try:
            dados = self._carregar_dados_user()

            email = input("Digite o email do paciente: ")
            usuario, index = self._buscar_usuario_por_email(email, dados)

            if usuario:
                remedio = input("Digite o nome do remédio a ser receitado: ")
                usuario.setdefault("Remedios_receitados", []).append(remedio)
                
                self._salvar_dados_user(dados)

                print(f"Remédio '{remedio}' receitado com sucesso para {usuario['Nome']}.")
                time.sleep(2)

            else:
                print(f"Usuário com o email {email} não encontrado.")
                time.sleep(2)

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao receitar remédio: {e}')

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

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')