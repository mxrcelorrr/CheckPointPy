valor_prod = float(input("Digite o valor do produto que deseja comprar "))


if valor_prod > 100:
    valor_prod = valor_prod * 0.9
    print(f"Como o valor passou dos 100 reais voce recebeu um desconto de 10%, então o preço do produto passa a ser {valor_prod}")
else:
    print(f"O valor a se pagar eh de {valor_prod}")