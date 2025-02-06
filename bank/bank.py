def main():

    resposta = input("Como posso ajudar? ")

    resposta = resposta.lower().strip()

    primeira_letra_h = resposta.startswith("h")

    if not primeira_letra_h:
        print("$100")
    elif "hello" in resposta:
        print("$0")
    else:
        print("$20")

main()

