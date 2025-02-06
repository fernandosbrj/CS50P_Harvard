def main():

    nome_arquivo = input("Digite o nome do arquivo: ").lower().strip()

    if ".gif" in nome_arquivo:
        print("image/gif")
    elif ".jpg" in nome_arquivo:
        print("image/jpeg")
    elif ".jpeg" in nome_arquivo:
        print("image/jpeg")
    elif ".png" in nome_arquivo:
        print("image/png")
    elif ".pdf" in nome_arquivo:
        print("application/pdf")
    elif ".txt" in nome_arquivo:
        print("text/plain")
    elif ".zip" in nome_arquivo:
        print("application/zip")
    else:
        print("application/octet-stream")

main()
