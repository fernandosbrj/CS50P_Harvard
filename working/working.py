import re

def main():

    try:
        print(convert(input("Hours: ")))
    except ValueError:
        raise

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM

def existe_minuto(min):
    if min is None:
        return False
    else:
        return True


def minutos_validos(m):
    m = int(m)
    if 0 <= m <= 59:
        return True
    else:
        raise ValueError("Minuto com valor inválido")


def hora_valida(h, ampm):
    h = int(h)
    if (h > 12 or h < 1):
        raise ValueError("Hora com valor inválido")
    else:
        return True



def convert_am_pm(hora, ampm):
    hora = int(hora)
    if ampm == "PM":
        if hora == 12:
            valor_hora = hora
        else:
            valor_hora = hora + 12

    if ampm == "AM":
        if hora == 12:
            valor_hora = 0
        else:
            valor_hora = hora
    return valor_hora


def convert(s):
    pattern = r"^([0-9]{1,2})(:([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(:([0-9]{2}))? (AM|PM)$"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError("Formato de hora não compatível")

    if matches:
        minuto1 = matches.group(3)
        minuto2 = matches.group(7)
        hora1 = matches.group(1)
        hora2 = matches.group(5)
        ampm1 = matches.group(4)
        ampm2 = matches.group(8)

        if existe_minuto(minuto1):
            if minutos_validos(minuto1) and hora_valida(hora1, ampm1):
                hora_final1 = convert_am_pm(hora1, ampm1)
                parte1 = f"{hora_final1:02}:{minuto1} to "

        if not existe_minuto(minuto1):
            if hora_valida(hora1, ampm1):
                hora_final1 = convert_am_pm(hora1, ampm1)
                parte1 = f"{hora_final1:02}:00 to "

        if existe_minuto(minuto2):
            if minutos_validos(minuto2) and hora_valida(hora2, ampm2):
                hora_final2 = convert_am_pm(hora2, ampm2)
                parte2 = f"{hora_final2:02}:{minuto2}"

        if not existe_minuto(minuto2):
            if hora_valida(hora2, ampm2):
                hora_final2 = convert_am_pm(hora2, ampm2)
                parte2 = f"{hora_final2:02}:00"

        hora_final = parte1 + parte2
        return hora_final

if __name__ == "__main__":
    main()
