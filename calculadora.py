def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return  a - b
    elif operador == "*":
        return  a * b
    elif operador == "/":
        if b == 0:
            raise ZeroDivisionError ("Não é possível dividir por zero")
        return a / b
    elif operador == "**":
         return a ** b
    elif operador == "%":
         if b == 0:
             raise ZeroDivisionError ("Não é possível dividir por zero")
         return a%b
    elif operador == "//":
         if b == 0:
             raise ZeroDivisionError ("Não é possível dividir por zero")
         return a // b
    
    else:
        raise ValueError (f"Operador inválido: '{operador}'")


def main():
    print("=== Calculadora ===")
    print("Digite 'sair' quando quiser encerrar.\n")

    while True:
        comando = input("Aperte ENTER para fazer uma conta ou digite 'sair': ").strip().lower()

        if comando == "sair":
            print("Até logo!")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /, **, %, //): ")
            num2 = float(input("Digite o segundo número: ")) 

            resultado = calcular(num1, num2, operador)
            print("Resultado:" , resultado)

        except ValueError as erro:
            print("Erro:", erro)
      
        except ZeroDivisionError:
            print("Erro:" , erro)

        except OverflowError:
            print("Erro: O número resultante é grande demais para ser calculado. \n")    


if __name__ == "__main__":
    main()
