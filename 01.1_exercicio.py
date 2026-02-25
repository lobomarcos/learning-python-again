nome_produto = str (input("Digite o nome do produto: "))
preco_produto = float (input("Digite o preço do produto: "))
quant_produto = int (input("Digite a quantidade de produtos no estoque: "))

valor_total = quant_produto * preco_produto

print (f"Há {quant_produto} unidades de {nome_produto} em estoque no valor de {preco_produto}. O valor total é: R$ {valor_total}.")