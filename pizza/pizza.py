import sys, csv, os
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        raise sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        raise sys.exit("Too many command-line arguments")
    file = sys.argv[1]
    if not os.path.exists(file):
        raise sys.exit("File does not exist") #I decided to simplify by using os instead of try/except to check if file path is valid
    elif not file.endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        table = create_table(file)
        print(table)


def create_table(file):
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        rows = list(reader) #Turned the document in a list of lists
    return tabulate(rows[1:], headers=rows[0], tablefmt="grid") #Set everything below row 1 as data and set row 0 as header in order to add === below it using grid


if __name__ == '__main__':
    main()
