def main():

    palavras = input("Digite algo: ").strip()
    lista_palavras = palavras.split()
    lista_sem_vogal = []
    for palavra in lista_palavras:
        lista_sem_vogal.append(shorten(palavra))

    print(" ".join(lista_sem_vogal))


def shorten(word):

    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    palavra_nova = []
    for i in range(len(word)):
        if word[i] not in lista_vogais:
            palavra_nova.append(word[i])

    return "".join(palavra_nova)



if __name__ == "__main__":
    main()
