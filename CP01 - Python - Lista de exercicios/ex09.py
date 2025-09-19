temp = int(input("Me de uma temperatura em graus celsius "))

if temp < 0:
    print("Congelante")
elif 0 <= temp <=30:
    print("Agradavel")
else:
    print("Quente")