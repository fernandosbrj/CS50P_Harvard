# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

import csv
import sys
from tabulate import tabulate



def main():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as csv_file:

            reader = csv.DictReader(csv_file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()


