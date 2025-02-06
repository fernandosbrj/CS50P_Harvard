import sys

def main():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:

        with open(sys.argv[1], "r") as arquivo_python:
            linhas = arquivo_python.readlines()

            qtde_linhas = 0
            for linha in linhas:
                if not (comentario(linha) or linha_em_branco(linha)):
                    qtde_linhas += 1

            print(qtde_linhas)

    except FileNotFoundError:
        sys.exit("File does not exist")


def comentario(l):
    l = l.strip()
    if l.startswith("#"):
        return True
    else:
        return False

def linha_em_branco(l):
    l = l.strip()
    if len(l) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
