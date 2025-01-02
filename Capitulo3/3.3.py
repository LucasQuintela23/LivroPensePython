def print_line():
    # Linha horizontal com '+ - - - - + - - - - +'
    print('+', '- ' * 4, '+', '- ' * 4, '+', sep='')

def print_vertical():
    # Linha vertical com '|         |         |', repetida 4 vezes
    for _ in range(4):
        print('|', ' ' * 9, '|', ' ' * 9, '|', sep='')

def draw_grid():
    # Desenha a grade completa
    print_line()       # Linha superior
    print_vertical()   # Linhas verticais abaixo
    print_line()       # Linha intermediária
    print_vertical()   # Linhas verticais abaixo
    print_line()       # Linha inferior

# Testando a função
draw_grid()
