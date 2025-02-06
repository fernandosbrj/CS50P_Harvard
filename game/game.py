def main():

    import random, sys

    while True:
        n = input("Level: ")

        if n.isnumeric():
            n = int(n)
            if n > 0:
                break


    alvo = random.randint(1,n)
    print(f"alvo: {alvo}")

    while True:

        palpite = input("Guess: ")
        if palpite.isnumeric():
            palpite = int(palpite)

            if palpite < alvo:
                print("Too small!")
            elif palpite > alvo:
                print("Too large!")
            else:
                print("Just Right!")
                sys.exit()

main()














main()
