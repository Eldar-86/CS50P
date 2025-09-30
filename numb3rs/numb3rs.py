import re

"""
def main(): #This version of the code checks validity of IPv4 address without the use of any additional libraries
    print(validate(input("IPv4 Address: ").strip().replace(" ", "")))


def validate(ip):
    try:
        a, b, c, d = ip.split(".")
        for part in [a, b, c, d]:
            if part.isalpha():
                return False
            elif part.startswith("0") and len(part) > 1:
                return False

        a, b, c, d = map(int, [a, b, c, d])
        for part in [a, b, c, d]:
            if part < 0 or part > 255:
                return False
        else:
            return True

    except ValueError:
        return False


if __name__ == '__main__':
    main()
"""



def main(): #This version of the code checks validity of IPv4 address with re library
    print(validate(input("IPv4 Address: ").strip().replace(" ", "")))


def validate(ip):
    if re.match(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", ip):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
