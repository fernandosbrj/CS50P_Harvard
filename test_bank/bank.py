def main():

    resposta = input("Como posso ajudar? ")
    resposta = resposta.strip()

    print(f"${value(resposta)}")


def value(greeting):

    primeira_letra_h = greeting.lower().startswith("h")

    if not primeira_letra_h:
        return 100
    elif "hello" in greeting:
        return 0
    else:
        return 20


if __name__ == "__main__":
    main()

