def main():

    horario = input("What time is it? ")
    horario = convert(horario)

    if 7 <= horario <= 8:
        print("breakfast time")

    if 12 <= horario <= 13:
        print("lunch time")

    if 18 <= horario <= 19:
        print("dinner time")


def convert(time):

    time = time.strip()
    horas, minutos = time.split(sep = ":")
    horas = float(horas)
    minutos = float(minutos) / 60

    total_em_horas = horas + minutos

    return total_em_horas


if __name__ == "__main__":
    main()
