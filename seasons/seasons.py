import re
import sys
import inflect
from datetime import date




def main():

    nascimento = input("Date of Birth: ")

    ano, mes, dia = formato_valido(nascimento)

    if mes_valido(mes) and dia_valido(dia, mes):
        data_nascimento = date(ano, mes, dia)
        hoje = date.today()
        idade = hoje - data_nascimento

        idade_em_minutos = round(idade.total_seconds() / 60)

        p = inflect.engine()
        words = p.number_to_words(idade_em_minutos, andword="").capitalize()
        print(f"{words} minutes")


    else:
        sys.exit("Invalid date")




def formato_valido(data):
    pattern = r"^([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})$"

    matches = re.search(pattern, data)
    if not matches:
        sys.exit("Invalid date")
    else:
        ano = int(matches.group(1))
        mes = int(matches.group(2))
        dia = int(matches.group(3))

        return ano, mes, dia


def mes_valido(m):
    if 1 <= m <= 12:
        return True
    else:
        return False

def dia_valido(d, m):

    if m < 1 or m > 12:
        return False

    if int(m) in [1,3,5,7,8,10,12]:
        if 1 <= d <= 31:
            return True
        else:
            return False

    elif int(m) in [4,6,9,11]:
        if 1 <= d <= 30:
            return True
        else:
            return False

    elif int(m) == 2:
        if 1 <= d <= 29:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
