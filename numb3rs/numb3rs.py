import re

def main():
    print(validate(input("IPv4 Address: ")))

def num_valido(num):
    if 0 <= int(num) <= 255:
        return True
    else:
        return False


def validate(ip):

    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    matches = re.search(pattern, ip)

    if matches:
        num1, num2, num3, num4 = ip.split(".")
        if (num_valido(num1) and
            num_valido(num2) and
            num_valido(num3) and
            num_valido(num4)):
            return True
        else:
            return False

    else:
        return False



if __name__ == "__main__":
    main()
