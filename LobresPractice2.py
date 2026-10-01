while True:
    name = input("ENTER YOUR NAME: ")

    print("Hello," , name)

    again = input("Do you want to enter again? (Y/N)")

    if again.upper() != "Y":
        print("Proper ended.")
        break
