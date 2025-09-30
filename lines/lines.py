import sys, os


def main():
    if len(sys.argv) < 2:
        raise sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        raise sys.exit("Too many command-line arguments")
    file = sys.argv[1]
    if not os.path.exists(file):
        raise sys.exit("File does not exist")
    elif not file.endswith(".py"):
        sys.exit("Not a Python file")
    else:
        number_of_lines = line_count(file)
        print(number_of_lines)


def line_count(file_name):
    loc = 0
    with open(file_name, "r") as file:
        for line in file:
            if not line.strip().startswith("#") and line.strip():
                loc +=1
    return loc


if __name__ == '__main__':
    main()
