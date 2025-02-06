def main():


    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    palavras = input("Digite algo: ")
    lista_letras = list(palavras)
    lista_sem_vogal = []

    for i in range(len(lista_letras)):

        if lista_letras[i] not in lista_vogais:
            lista_sem_vogal.append(lista_letras[i])

    sentenca_sem_vogal = "".join(lista_sem_vogal)
    print(sentenca_sem_vogal)



main()
