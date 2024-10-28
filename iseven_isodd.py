
while True:

    number = input(f"Please input a number ")


    if number == "":
        print(f"Please input a number")
        number = int(input(f"Please input a number "))
    else:
        if float(number) % 2 == 0:
            iseven = True
        else:
            iseven = False

    print("Its even" if iseven else "Its odd")