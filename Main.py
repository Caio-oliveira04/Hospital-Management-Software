from Usuario import Usuario

print('1 - Cadastre-se'   )
print('2 - Fazer Loguin'   )
print('3 - Marcar consulta' )
print('4 - Remarcar consulta')
print('5 - Desmarcar consulta')
print('6 - Sair'               )

escolha = input('Digite a Opção desejada: ')
usuario1 = Usuario()

if escolha == '1':
    nome = input('Digite seu nome: '   )
    email = input('Diggite seu Email: ')
    senha = input('Digite sua senha: ' )
    usuario1.set_nome(nome)
    usuario1.set_email(email)
    usuario1.set_senha(senha)
    usuario1.cadastro_user(nome, email, senha)

if escolha == '2':
    email = input('Diggite seu Email: ')
    senha = input('Digite sua senha: ' )
    usuario1.set_email(email)
    usuario1.set_senha(senha)
    usuario1.login_user(email, senha)

