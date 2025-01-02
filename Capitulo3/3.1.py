# Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e 
# exiba a string com espaços suficientes à frente para que a última letra 
# da string esteja na coluna 70 da tela:
def right_justify(s):
    # Calcula o número de espaços necessários para a última letra estar na coluna 70
    espacos = 70 - len(s)
    # Gera a string com os espaços à frente
    resultado = ' ' * espacos + s
    # Exibe a string
    print(resultado)

# Testando a função
right_justify('monty')
right_justify("teste")
right_justify('python')
right_justify('QA')
