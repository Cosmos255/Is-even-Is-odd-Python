

def is_even_is_odd(number=None):
    try:
        if number is None:
            number = input(f"Please input a number (q to quit) ").lower()

        if number == "q":
            exit()

        else:

            if float(number) % 2 == 0:
                print("Its even")
            else:
                print("Its odd")

        is_even_is_odd()
    except Exception:
        print(f"Please input a valid number")
        is_even_is_odd()


if __name__ == "__main__":
    print(is_even_is_odd())
