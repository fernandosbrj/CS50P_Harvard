def main():

    resposta = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    resposta = resposta.lower().strip()

    if resposta == "42" or resposta == "forty-two" or resposta == "forty two":
        print("Yes")
    else:
        print("No")

main()
