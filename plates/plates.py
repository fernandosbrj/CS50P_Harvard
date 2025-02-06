"""
“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.

The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def inicia_2letras(placa):
        if placa[:2].isalpha():
            return True
        else:
            return False

def entre_2e6(placa):
    if 2 <= len(placa) <= 6:
         return True
    else:
         return False

def num_por_ultimo(placa):
     if placa.isalpha():
        return True
     total_num = 0
     for i in range(len(placa)):
          if placa[i].isdigit():
               total_num += 1

     ultimos_char = placa[-total_num:]
     if ultimos_char.isdigit():
          return True
     else:
          return False

def first_number_notzero(placa):
     if placa.isalpha():
          return True
     for i in range(len(placa)):
          if placa[i].isdigit():
               if placa[i] != "0":
                    return True
               else:
                    return False

def todos_alphanum(placa):
     if placa.isalnum():
          return True
     else:
          return False

def is_valid(s):

     a = inicia_2letras(s)
     b = entre_2e6(s)
     c = num_por_ultimo(s)
     d = first_number_notzero(s)
     e = todos_alphanum(s)

     if a and b and c and d and e:
          return True
     else:
          return False





main()
