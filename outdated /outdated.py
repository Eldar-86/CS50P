month = {"January": 1,
         "February": 2,
         "March": 3,
         "April": 4,
         "May": 5,
         "June": 6,
         "July": 7,
         "August": 8,
         "September": 9,
         "October": 10,
         "November": 11,
         "December": 12}


while True:
    user_input = input("Date: ").capitalize().strip()

    if "/" not in user_input and "," not in user_input:
        continue

    elif "/" in user_input and "," in user_input:
        continue

    elif "," in user_input:
        user_input = user_input.replace(",", "")
        m, d, y = user_input.split(" ")
        if d.isalpha():
            continue
        elif d.isdigit():
            d = int(d)
            if d >31:
                continue
            else:
                print(f"{y}-{month[m]:02}-{d:02}")
        break

    elif "/" in user_input and "," not in user_input and " " not in user_input:
        m, d, y = user_input.split("/")
        if m.isalpha():
            continue
        elif m.isdigit() and d.isdigit():
            m, d = int(m), int(d)
            if m<13 and d<32:
                print(f"{y}-{m:02}-{d:02}")
                break
            else:
                continue
