def main():

    valor_coca = 50
    valor_total_depositado = 0

    while valor_total_depositado < valor_coca:

        valor_faltante = valor_coca - valor_total_depositado
        print(f"Amount Due: {valor_faltante}")
        moeda_inserida = int(input("Insert Coin: "))

        if moeda_permitida(moeda_inserida):
            valor_total_depositado += moeda_inserida
            valor_faltante = valor_coca - valor_total_depositado

            if valor_faltante <= 0:
                print(f"Change Owed: {-valor_faltante}")
                break



def moeda_permitida(moeda):
    moedas_permitidas = [25,10,5]
    if moeda in moedas_permitidas:
        return True
    else:
        return False



main()
