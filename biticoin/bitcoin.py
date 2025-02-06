def main():

    import sys
    import requests

    # verifica se o usuário digitou um argumento e se a entrada pode ser convertida para float.
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    else:
        try:
            qtde_bitcoins = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    # requisição para o site de bitcoin
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # conversão do objeto tipo "requests" para dicionário utilizando .json()
        response = response.json()

    except requests.RequestException:
        print(response.status_code)

    else:
        valor_bitcoin_em_dolar = response["bpi"]["USD"]["rate"]

        # retirar vírgula da string para que seja possível convertê-la em float
        valor_bitcoin_em_dolar = valor_bitcoin_em_dolar.replace(",", "")

        valor_bitcoin_em_dolar = float(valor_bitcoin_em_dolar)

        total = valor_bitcoin_em_dolar * qtde_bitcoins
        print(f"${total:,.4f}")
        sys.exit()


if __name__ == "__main__":
    main()
