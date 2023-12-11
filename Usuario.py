import json
import pathlib
import os
import time
import hashlib

class Usuario:
    CLIENTES_FILE = "clientes.txt"

    def __init__(self):
        self.nome = ""
        self.email = ""
        self.senha = ""
        self.saldo = None

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_senha(self, senha):
        self.senha = senha

    def get_senha(self):
        return self.senha

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def cadastro_user(self, nome, email, senha):
        try:
            dados = self._carregar_dados()

            novo_usuario = {
                "Nome": nome,
                "Email": email,
                "Senha": self._hash_senha(senha),
                "Consultas": [],
                "Saldo": 0,  
                "Exames_solicitados":[],
                "Exame_feitos":[],
                "Remedios_receitados":[],
                "Remedios_comprados":[]
            }

            dados.append(novo_usuario)

            self._salvar_dados(dados)

            self.clear_screen()
            print('Cadastro feito com sucesso')
            time.sleep(2)
            
        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def login_user(self, email, senha):
        try:
            dados = self._carregar_dados()

            for usuario in dados:
                if usuario["Email"] == email and usuario["Senha"] == self._hash_senha(senha):
                    print("Login feito com sucesso!")
                    return
                elif usuario["Email"] == email and usuario["Senha"] != senha:
                    print("Senha incorreta")
                    return
                elif usuario["Email"] != email and usuario["Senha"] == senha:
                    print("Email incorreto")
                    return

            print("Email não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao realizar login: {e}')

    def marcar_consulta(self):
        try:
            dados = self._carregar_dados()

            email = input("Digite seu email: ")
            usuario, index = self._buscar_usuario_por_email(email, dados)

            if usuario:
                especialista = int(input("Selecione o especialista:\n"
                                         "1 - Cardiologista\n"
                                         "2 - Dermatologista\n"
                                         "3 - Ginecologista\n"
                                         "4 - Neurologista\n"
                                         "5 - Pediatra\n"
                                         "6 - Sair\n"))

                if especialista == 6:
                    return

                elif 1 <= especialista <= 5:
                    especialidades = ['Cardiologista', 'Dermatologista', 'Ginecologista', 'Neurologista', 'Pediatra']
                    especialista_escolhido = especialidades[especialista - 1]

                    especialidades_valor = [150, 100, 200, 300, 100]
                    valor = especialidades_valor[especialista - 1]

                    data_desejada = input('Digite a data desejada (DD/MM/YYYY): ')

                    nova_consulta = f"{especialista_escolhido} {data_desejada}"
                    usuario["Consultas"].append(nova_consulta)

                    self._salvar_dados(dados)

                    if valor <= usuario["Saldo"]:
                        usuario["Saldo"] -= valor
                        self._salvar_dados(dados)
                        self.clear_screen()
                        print('Consulta marcada com sucesso!')
                        time.sleep(2)
                    else:
                        print('Saldo insuficiente, adicione dinheiro a sua carteira')
                        self.adiocionar_dinheiro()

                else:
                    print('Especialista inválido')

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao marcar a consulta: {e}')


    def remarcar_consulta(self):
        try:
            dados = self._carregar_dados()

            email = input("Digite seu email: ")
            usuario, index = self._buscar_usuario_por_email(email, dados)

            if usuario:
                data_antiga = input('Digite a data a ser alterada: ')
                nova_data = input('Digite a nova data para a consulta: ')

                consultas = usuario.get("Consultas", [])
                encontrada = False

                for i, consulta in enumerate(consultas):
                    if data_antiga in consulta:
                        consultas[i] = consulta.replace(data_antiga, nova_data)
                        encontrada = True
                        print(f"Data da consulta atualizada: {consulta} -> {consultas[i]}")
                        break

                if not encontrada:
                    print(f"Nenhuma consulta encontrada para a data {data_antiga}")

                self._salvar_dados(dados)

                self.clear_screen()
                print('Consulta remarcada com sucesso!')
                time.sleep(2)

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao remarcar a consulta: {e}')

    def desmarcar_consulta(self):
        try:
            dados = self._carregar_dados()

            email = input("Digite seu email: ")
            usuario, index = self._buscar_usuario_por_email(email, dados)

            if usuario:
                data_antiga = input('Digite a data da consulta a ser desmarcada: ')

                consultas = usuario.get("Consultas", [])
                encontrada = False

                for i, consulta in enumerate(consultas):
                    if data_antiga in consulta:
                        consultas.remove(consulta)
                        encontrada = True
                        print(f"Consulta desmarcada: {consulta}")
                        break

                if not encontrada:
                    print(f"Nenhuma consulta encontrada para a data {data_antiga}")

                self._salvar_dados(dados)

                self.clear_screen()
                print('Consulta desmarcada com sucesso!')
                time.sleep(2)

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao desmarcar a consulta: {e}')

    def print_exames_solicitados_e_marcar_exame(self):
        try:
            dados = self._carregar_dados()

            email = input("Digite seu email: ")
            usuario, index = self._buscar_usuario_por_email(email, dados)

            if usuario:
                exames_solicitados = usuario.get("Exames_solicitados", [])

                if exames_solicitados:
                    print("Exames solicitados:")
                    for i, exame in enumerate(exames_solicitados, start=1):
                        print(f"   -> Exame {i}: {exame}")
                    
                    marcar = input('Deseja marcar algum desses exames? ')
                    if marcar.lower() == 'sim':
                        exame_a_ser_marcado = input('Qual exame deseja marcar? ')
                        if exame_a_ser_marcado in exames_solicitados:
                            exames_solicitados.remove(exame_a_ser_marcado)
                            data = input('Qual a data a ser marcada para o exame? ')
                            resultado = 'Ainda sem resultado'
                            exame_marcado = {"Exame": exame_a_ser_marcado, "Data": data, "Resultado": resultado}
                            usuario.setdefault("Exames_feitos", []).append(exame_marcado)
                            dados[index] = usuario
                            self._salvar_dados(dados)
                            print(f"Exame {exame_a_ser_marcado} marcado com sucesso para a data {data}.")
                        else:
                            print("Exame não encontrado na lista de exames solicitados.")
                    else:
                        print("Nenhum exame marcado.")

                else:
                    print("Nenhum exame solicitado.")
            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao imprimir/examinar exames solicitados: {e}')

    def print_resultados_exames(self):
        try:
            dados = self._carregar_dados()

            email = input("Digite seu email: ")
            usuario, _ = self._buscar_usuario_por_email(email, dados)

            if usuario:
                exames_feitos = usuario.get("Exames_feitos", [])

                if exames_feitos:
                    print("Resultados dos Exames:")
                    for i, exame in enumerate(exames_feitos, start=1):
                        print(f"   -> Exame {i}: {exame['Exame']}")
                        print(f"      Data: {exame['Data']}")
                        print(f"      Resultado: {exame['Resultado']}")
                else:
                    print("Nenhum resultado de exame disponível.")

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao imprimir resultados de exames: {e}')

    def print_remedios_receitados(self):
        try:
            dados = self._carregar_dados()

            email = input("Digite seu email: ")
            usuario, _ = self._buscar_usuario_por_email(email, dados)

            if usuario:
                remedios_receitados = usuario.get("Remedios_receitados", [])

                if remedios_receitados:
                    print("Remédios Receitados:")
                    for i, remedio in enumerate(remedios_receitados, start=1):
                        print(f"   -> Remédio {i}: {remedio}")
                else:
                    print("Nenhum remédio receitado.")

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao imprimir remédios receitados: {e}')

    def adiocionar_dinheiro(self):
            try:
                email_alvo = input('Digite o email da pessoa para adicionar dinheiro: ')
                deposito = float(input('Quanto deseja adicionar na sua carteira?'))

                dados = self._carregar_dados()
                usuario_alvo, _ = self._buscar_usuario_por_email(email_alvo, dados)

                if usuario_alvo:
                    usuario_alvo["Saldo"] += deposito
                    self._salvar_dados(dados)

                    self.clear_screen()
                    print(f'Dinheiro adicionado com sucesso para {usuario_alvo["Nome"]}')
                    time.sleep(2)

                else:
                    print('Usuário não encontrado.')

            except ValueError:
                print('Valor inválido. Certifique-se de inserir um número válido.')

    def _carregar_dados(self):
        if pathlib.Path(self.CLIENTES_FILE).exists():
            with open(self.CLIENTES_FILE, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _salvar_dados(self, dados):
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

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')