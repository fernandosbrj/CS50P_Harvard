def main():

    expressao = input("Digite uma expressão: ").strip()

    primeiro_num, sinal, segundo_num = expressao.split()
    primeiro_num = float(primeiro_num)
    segundo_num = float(segundo_num)

    match sinal:
        case "+":
            soma = primeiro_num + segundo_num
            print(f"{soma:.1f}")

    match sinal:
        case "-":
            subtracao = primeiro_num - segundo_num
            print(f"{subtracao:.1f}")

    match sinal:
        case "*":
            multipliacao = primeiro_num * segundo_num
            print(f"{multipliacao:.1f}")

    match sinal:
        case "/":
            divisao = primeiro_num / segundo_num
            print(f"{divisao:.1f}")

main()
