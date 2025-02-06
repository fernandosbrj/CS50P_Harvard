def main():

    import sys
    import inflect
    p = inflect.engine()

    lista_nomes = []

    try:
        while True:
            nome = input()
            lista_nomes.append(nome)

    except EOFError:
        pass

    finally:

        frase = p.join(lista_nomes)
        print(f"Adieu, adieu, to " + frase)
        sys.exit()

main()






















if __name__ == "__main__":
    main()

