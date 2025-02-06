import sys

def main():
    while True:
        fracao = input("Fraction: ").strip()
        percentual = convert(fracao)

        tanque = gauge(percentual)
        print(tanque)
        sys.exit()



def convert(fraction):

    try:
        numerador, denominador = fraction.split(sep = "/")
        numerador = numerador.strip()
        denominador = denominador.strip()

        numerador = int(numerador)
        denominador = int(denominador)

        if denominador == 0:
            raise ZeroDivisionError

        if numerador > denominador:
            raise ValueError

        percentual = (numerador / denominador) * 100
        return percentual

    except (ValueError):
        raise



def gauge(percentage):

    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    if 1 < percentage < 99:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
