def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(msg):
    print(msg)
    print(msg)

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

# Testes
print("Testando do_twice:")
do_twice(print_twice, 'spam')

print("\nTestando do_four:")
do_four(print_twice, 'spam')
