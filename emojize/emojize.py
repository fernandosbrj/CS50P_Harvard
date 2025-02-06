def main():

    import emoji

    emoji_string = input().strip()
    print(emoji.emojize(emoji_string, language = "alias"))


if __name__ == "__main__":
    main()

