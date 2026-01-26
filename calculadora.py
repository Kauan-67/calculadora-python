def calculadora():
    print("bem vindo a calculadora!".capitalize())
    conta = input("Qual conta deseja fazer?").lower()
    if conta == "Multiplicacao" or conta == "x" or conta == "*":
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        so = num1 * num2
        print(so)
    elif conta == "Adição" or conta == "+" or conta == "mais":
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
        soma = n1 + n2
        print(soma)
    
    elif conta == "Divisão" or conta == "dividir":
        nr1 = int(input("Digite um numero: "))
        nr2 = int(input("Digite outro numero: "))
        sm = nr1 / nr2
        print(sm)

    elif conta == "Subtração" or conta == "-" or conta == "menos":
        numero1 = int(input("DIgite um numero: "))
        numero2 = int(input("Digite outro numero: "))
        result = numero1 - numero2
        print(result)
    elif conta == "porcentagem" or conta == "%":
        v1 = int(input("DIgite o primeiro valor: "))
        v2 = int(input("Digite o valor para aplicar a porcentagem:"))
        total = v1 * (v2 / 100)
        print(f"total {total:.2f}")
    else:
        print("opçao invalida!")
calculadora()
