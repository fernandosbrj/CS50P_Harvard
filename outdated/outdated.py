months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    while True:

        date = input("Date: ").strip()

        if date_in_short_format(date):
            month, day, year = date.split("/")

            if month_1_to_12(month) and day_1_to_31(day):
                print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                break

        if date_in_long_format(date):
            month, day, year = date.split(" ")
            day = day.removesuffix(",")
            if day_1_to_31(day):
                month_index = months.index(month) + 1
                month_index = str(month_index)
                print(f"{year}-{month_index.zfill(2)}-{day.zfill(2)}")
                break

# verifica se o número do mês está entre 1 e 12
def month_1_to_12(m):
    m = int(m)
    if 1 <= m <= 12:
        return True
    else:
        return False

# verifica se o número do dia está entre 1 e 31
def day_1_to_31(d):
    d = int(d)
    if 1 <= d <= 31:
        return True
    else:
        return False

# verifica se a data está no formato abreviado XX/XX/XXXX
def date_in_short_format(date_short):
    if date_short.count("/") == 2:
        m, d, y = date_short.split("/")
        # verifica se mes, dia e ano podem ser convertidos em números
        try:
            m = int(m)
            d = int(d)
            y = int(y)
        except ValueError:
            pass
        else:
            return True
# verifica se a data está no formato "mês_por_extenso dia, ano"
def date_in_long_format(date_long):
    if date_long.count(",") == 1:
        month, day, year = date_long.split(" ")
        day = day.removesuffix(",")
        try:
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            if month in months:
                return True

main()
