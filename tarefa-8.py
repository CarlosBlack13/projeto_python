preco_produto1 = float(input("Digite o preço do primeiro produto: R$ "))
preco_produto2 = float(input("Digite o preço do segundo produto: R$ "))
preco_produto3 = float(input("Digite o preço do terceiro produto: R$ "))


menor_preco = min(preco_produto1, preco_produto2, preco_produto3)


if menor_preco == preco_produto1:
    produto_mais_barato = "primeiro produto"
elif menor_preco == preco_produto2:
    produto_mais_barato = "segundo produto"
else:
    produto_mais_barato = "terceiro produto"


print(f"O produto mais barato é o {produto_mais_barato}, com o preço de R$ {menor_preco:.2f}.")
