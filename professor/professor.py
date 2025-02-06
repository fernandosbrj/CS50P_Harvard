import random


def main():

    num_digitos = get_level()
    total_de_questoes = 10
    qtde_acertos = 0
    qtde_erros = 0

    for i in range(total_de_questoes):
        
        x = generate_integer(num_digitos)
        y = generate_integer(num_digitos)
        qtde_erros = 0
        resposta_correta = x + y

        # apresenta a questão para o usuário
        resposta_usuario = input(f"{x} + {y} = ")
        while True:
            try:
                resposta_usuario = int(resposta_usuario)
                if resposta_usuario == resposta_correta:
                    qtde_acertos += 1
                    break
                else:
                    print("EEE")
                    qtde_erros += 1
                    if qtde_erros == 3:
                        print(f"{x} + {y} = {resposta_correta}")
                        break
                    resposta_usuario = input(f"{x} + {y} = ")

            except ValueError:
                pass
    print(f"Score: {qtde_acertos}")


def get_level():
    while True:
        level = input()
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    try:
        if level == 1:
            return(random.randint(0,9))
        if level == 2:
            return(random.randint(10,99))
        if level == 3:
            return(random.randint(100,999))
    except ValueError:
        print("ValueError")


if __name__ == "__main__":
    main()
