import re


def main():
    print(count(input("Text: ")))


def count(s):

    pattern = r"\bum\b"
    lista_matches = re.findall(pattern, s, re.IGNORECASE)

    return len(lista_matches)


if __name__ == "__main__":
    main()
