def main():


    import sys
    import random
    from pyfiglet import Figlet

    figlet = Figlet()
    lista_fontes = figlet.getFonts()

    if len(sys.argv) not in [1,3]:
        sys.exit("Invalid usage")

    if len(sys.argv) == 1:
        texto_usuario = input("digite alguma coisa: ").strip()
        fonte_escolhida = random.choice(lista_fontes)
        figlet.setFont(font = fonte_escolhida)
        print(figlet.renderText(texto_usuario))
        sys.exit()


    if len(sys.argv) == 3:

        comandos = ["-f", "--font"]

        fonte_escolhida = sys.argv[2]
        comando = sys.argv[1]

        if comando not in comandos or fonte_escolhida not in lista_fontes:
            sys.exit("Invalid usage")
        else:
            texto_usuario = input("digite alguma coisa: ").strip()
            figlet.setFont(font = fonte_escolhida)
            print(figlet.renderText(texto_usuario))
            sys.exit()

main()
