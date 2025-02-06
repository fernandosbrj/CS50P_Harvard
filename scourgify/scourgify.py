import sys
import csv

def main():

    if len(sys.argv) in [1, 2]:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[2].endswith(".csv"):
        sys.exit(f"{sys.argv[2]} is not a valid csv file")

    try:
        with open(sys.argv[1], "r") as before_file, open(sys.argv[2], "w") as after_file:
            reader = csv.DictReader(before_file)

            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(after_file, fieldnames = fieldnames)
            writer.writeheader()
            for row in reader:
                last_name, first_name = row['name'].split(",")
                first_name = first_name.strip()
                last_name = last_name.strip()
                house = row["house"]

                writer.writerow(
                    {
                        "first": first_name,
                        "last": last_name,
                        "house": house,
                    }
                )


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
