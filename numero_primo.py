numero = int(input("Escribe un número entero: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")
