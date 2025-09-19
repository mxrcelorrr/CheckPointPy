num1 = int(input("Digite um numero inteiro "))
num2 = int(input("Digite novamente um numero inteiro "))

if num1 > num2:
    print("O primeiro numero eh o maior da sessao")
elif num2 > num1:
    print("O segundo numero eh o maior da sessao")
else:
    print("Os numeros sao iguais")