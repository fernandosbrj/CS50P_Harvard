def main():
    name = input("Text something, please. ")
    convert(name)

def convert(text = ""):

    emoji_feliz = "\U0001F642"
    emoji_triste = "\U0001F641"
    text = text.replace(":)", emoji_feliz)
    text = text.replace(":(", emoji_triste)
    print(text)

main()
