# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

from datetime import datetime, timedelta

# Dados
hora_saida = datetime.strptime("06:52", "%H:%M")  # Horário de saída
passo_1_km = timedelta(minutes=8, seconds=15)     # Tempo por quilômetro (8min15s)
passo_3_km = timedelta(minutes=7, seconds=12)     # Tempo por quilômetro (7min12s)

# Cálculos
tempo_primeiro_km = passo_1_km  # Tempo para o 1º quilômetro
tempo_tres_km = passo_3_km * 3  # Tempo para os 3 quilômetros mais rápidos
tempo_ultimo_km = passo_1_km    # Tempo para o último quilômetro

# Tempo total da corrida
tempo_total = tempo_primeiro_km + tempo_tres_km + tempo_ultimo_km

# Horário de chegada
hora_chegada = hora_saida + tempo_total

# Exibindo o resultado
print(f"Você chegará em casa às {hora_chegada.strftime('%H:%M:%S')} para o café da manhã.")
