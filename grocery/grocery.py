def main():

    lista_itens = dict()
    try:
        while True:

            item = input().strip().upper()
            if len(lista_itens) == 0:
                lista_itens[item] = 1
            else:
                if item not in lista_itens:
                    lista_itens[item] = 1
                else:
                    lista_itens[item] += 1

    except ValueError:
        pass
    except EOFError:
        chaves_ordenadas = sorted(lista_itens)
        for chave in chaves_ordenadas:
            print(f"{lista_itens[chave]} {chave}")
        return


main()















