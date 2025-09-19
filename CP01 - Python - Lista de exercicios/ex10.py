numero1 = int(input("Digite numero inteiro "))
numero2 = int(input("Digite novamente um numero inteiro "))
oper = input("Escolha uma dessas operaçoes matematicas (+, -, *, /): ")

if oper == '*':
    print(numero1 * numero2)
elif oper == '/':
    if numero1 and numero2 != 0:
        print(numero1 / numero2)
    else:
        print("nao eh possivel dividir um numero por zero")
elif oper == '+':
    print(numero1 + numero2)
elif oper == '-':
    print(numero1 - numero2)
else:
    print("operacao invalida")
