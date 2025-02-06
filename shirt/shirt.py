import sys
from os import path
from PIL import Image, ImageOps

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    _, extension1 = path.splitext(sys.argv[1])
    _, extension2 = path.splitext(sys.argv[2])

    if extension1.lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if extension2.lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if extension1.lower() != extension2.lower():
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        before = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    else:
        size = shirt.size
        after = ImageOps.fit(before, size)
        after.paste(shirt, shirt) # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste
        after.save(sys.argv[2])


if __name__ == "__main__":
    main()
