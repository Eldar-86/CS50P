import re


def main():
    print(convert(input("Hour: ")))


def convert(s):
    match = re.match(r"^(\d{1,2}):?(\d{1,2})?\s(AM|PM)\sto\s(\d{1,2}):?(\d{1,2})? (AM|PM)$", s)
    if not match:
        raise ValueError

    h1 = int(match.group(1))
    m1 = int(match.group(2) or 0)
    h2 = int(match.group(4))
    m2 = int(match.group(5) or 0)
    period_1 = match.group(3)
    period_2 = match.group(6)

    if h1 < 0 or h1 > 12 or h2 < 0 or h2 > 12 or m1 < 0 or m1 > 59 or m2 < 0 or m2 > 59:
        raise ValueError

    if period_1 == "PM" and h1 != 12:
        h1 += 12
    elif period_1 == "AM" and h1 == 12:
        h1 = 0

    if period_2 == "PM" and h2 != 12:
        h2 += 12
    elif period_2 == "AM" and h2 == 12:
        h2 = 0

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
