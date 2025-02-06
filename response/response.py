import validators

def main():

    try:
        print(email_validation(input("What's your e-mail address: ")))
    except ValueError:
        print("Invalid")

def email_validation(email):

    email_address = validators.email(email)

    if email_address:
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()
