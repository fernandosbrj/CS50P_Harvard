import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z-0-9]{11})"
    matches = re.search(pattern, s)

    if matches:
        return f"https://youtu.be/" + matches.group(2)
    else:
        return None


if __name__ == "__main__":
    main()
