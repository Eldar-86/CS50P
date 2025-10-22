import datetime, inflect, re
import sys

p = inflect.engine()


def main():
    date_input = input("Date of birth:")
    match = re.match(r"\d{4}-\d{2}-\d{2}", date_input)
    if not match:
        sys.exit()
    else:
        print(convert(date_input))


def convert(date):
    y, m, d = date.split("-")
    user_date = datetime.date(int(y), int(m), int(d))
    current_date = datetime.date.today()
    days = current_date - user_date
    count = round(days.total_seconds() / 60)
    in_written = p.number_to_words(count).replace(" and ", " ").capitalize()

    return f"{in_written} minutes"


if __name__ == "__main__":
    main()
