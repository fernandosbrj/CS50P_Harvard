def main():

    camelcase = input("Digite algo no formato camelcase: ")

    lista_letras = list(camelcase)
    nova_lista = []

    for i in range(len(lista_letras)):

        if lista_letras[i].islower():
            nova_lista.append(lista_letras[i])
        else:
            nova_lista.append("_")
            letra_lower = lista_letras[i].lower()
            nova_lista.append(letra_lower)

    string_lowercase = "".join(nova_lista)
    print(string_lowercase)


main()


