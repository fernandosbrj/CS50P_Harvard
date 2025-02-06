menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    try:
        total = 0
        while True:
            pedido = input("Item: ").strip().title()
            if pedido in menu:
                total += menu[pedido]
                print(f"${total:.2f}")


    except EOFError:
        print("\n")
        print(f"""Muito Obrigado. O seu pedido foi realizado e o pagamento de ${total} foi recebido.""")

main()
