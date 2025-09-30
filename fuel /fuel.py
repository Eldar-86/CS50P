while True:
    try:
        expression = input("> ").replace(" ", "")
        x, z = expression.split("/")
        a = int(x)
        b = int(z)
        division = (a / b) * 100
        
        if -1 < division < 2:
            print("E")
        elif 2 < division < 98:
            print(f"{division:.0f}%")
        elif division < 0 or division > 100:
            continue
        elif 98 < division < 101:
            print("F")
        break

    except (ZeroDivisionError, ValueError):
        continue
