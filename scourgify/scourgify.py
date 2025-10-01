import sys, os, csv


def main():
    if len(sys.argv) < 3:
        raise sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        raise sys.exit("Too many command-line arguments")
    file = sys.argv[1]
    file1 = sys.argv[2]
    if not os.path.exists(file):
        raise sys.exit(f"Could not read {sys.argv[1]}")
    elif not file.endswith(".csv") or not file1.endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        taking_names(sys.argv[1])


def taking_names(document=""):
    with open(document, "r") as in_file:
        reader = csv.DictReader(in_file)

        with open(sys.argv[2], "w", newline='') as out_file:
            if not os.path.exists(sys.argv[2]):
                with open('after.csv', 'w'):
                    pass
            else:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(out_file, fieldnames=fieldnames)
                writer.writeheader()

            for row in reader:
                last, first = row['name'].split(',')
                house = row['house']
                last = last.strip()
                first = first.strip()
                house = house.strip()
                writer.writerow({'first': first,
                                 'last': last,
                                 'house': house})


if __name__ == '__main__':
    main()
