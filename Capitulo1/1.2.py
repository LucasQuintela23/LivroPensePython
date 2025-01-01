# Inicialize o interpretador do Python e use-o como uma calculadora.

# 1.Quantos segundos há em 42 minutos e 42 segundos?
# test1 = print(42 * 60 + 42)


# 2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
# test2 = print(10 / 1.61)

# 3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio 
# (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora? ""
# Dados

tempo_minutos = 42
tempo_segundos = 42
kilometros = 10

# Conversão de distância para milhas
milhas = kilometros / 1.61

# Conversão do tempo total para segundos
tempo_total_segundos = (tempo_minutos * 60) + tempo_segundos

# Cálculo do tempo por milha (em segundos)
tempo_por_milha_segundos = tempo_total_segundos / milhas

# Conversão do tempo por milha para minutos e segundos
tempo_por_milha_minutos = int(tempo_por_milha_segundos // 60)
tempo_por_milha_segundos = int(tempo_por_milha_segundos % 60)

# Conversão do tempo total para horas
tempo_total_horas = tempo_total_segundos / 3600

# Cálculo da velocidade média (milhas por hora)
velocidade_media = milhas / tempo_total_horas

# Resultados
print(f"Passo médio: {tempo_por_milha_minutos} minutos e {tempo_por_milha_segundos} segundos por milha.")
print(f"Velocidade média: {velocidade_media:.2f} milhas por hora.")
