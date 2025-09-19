login = input("Digite o seu login de acesso ")
senha = input("Digite a sua senha de acesso ")

if login == 'admin' and senha == '1234':
    print("Acesso permitido")
else:
    print("Acesso negado")