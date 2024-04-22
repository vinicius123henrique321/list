def fibonacci(numero):
    a = 0
    b = 1
    while b < numero:
        a = b
        b = a + b
    if b == numero:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar: "))

if fibonacci(numero):
    print(f"O número {numero} pertence a sequencia.")
else:
    print(f"O número {numero} não pertence a sequencia.")


