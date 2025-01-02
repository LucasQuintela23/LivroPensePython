# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

# Dados
preco_capa = 24.95
desconto = 0.40
custo_transporte_primeiro = 3.00
custo_transporte_adicional = 0.75
quantidade = 60

# Cálculo do preço com desconto
preco_com_desconto = preco_capa * (1 - desconto)

# Cálculo do custo total dos livros
custo_livros = preco_com_desconto * quantidade

# Cálculo do custo total de transporte
custo_transporte = custo_transporte_primeiro + (custo_transporte_adicional * (quantidade - 1))

# Cálculo do custo total
custo_total = custo_livros + custo_transporte

# Exibindo o resultado
print(f"O custo total de atacado para {quantidade} cópias é R$ {custo_total:.2f}")
