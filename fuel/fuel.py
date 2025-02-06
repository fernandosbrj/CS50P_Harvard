def main():

    while True:

        try:
            numerador, denominador = input("Fraction: ").strip().split(sep = "/")

            #if numerador.isdecimal() and denominador.isdecimal():
            numerador = int(numerador)
            denominador = int(denominador)
            fracao = numerador / denominador
            if numerador <= denominador:
                if fracao <= 0.01:
                    print("E")
                    break
                if fracao >= 0.99:
                    print("F")
                    break
                if 0.01 < fracao < 0.99:
                    print(f"{int(round(fracao * 100, 0))}%")
                    break

        except ValueError:
            print(f"""
            Os dados informados não estão no padrão permitido.
            1 - Os valores do numerador (X) e denominador (Y) são inteiros e devem
                ser inseridos no formato 'X/Y'.
            2 - O numerador deve ser igual ou menor que o denominador.
            """)

        except ZeroDivisionError:
            print(f"Não é possível dividir por zero, seu idiota.")

main()
