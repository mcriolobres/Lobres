LOBRES_students = [
    ("Jonah Perez", "BSCS", 1),
    ("Alex Santos", "BSMT", 2),
    ("Patrick Star", "BSCS", 3),
    ("Allen Kalbo", "BSMT", 4),
    ("Sean Ethan", "BSCS", 4),
    ("Kuin Oh", "BSMT", 3),
    ("Micah Mendoza", "BSCS", 2),
    ("Allen Torres", "BSMT", 1)
]

print(f"\n{'Student Information:':=^40}")

while True:

    LOBRES_search_program = input("Enter Program (BSCS/BSMT): ")
    LOBRES_search_year = int(input("Enter Year Level (1-4): "))

    found = False

    for LOBRES_student in LOBRES_students:

        if LOBRES_student[1].upper() == LOBRES_search_program.upper() and LOBRES_student[2] == LOBRES_search_year:

            print("\nStudent Found!")
            print("Name:", LOBRES_student[0])
            print("Program:", LOBRES_student[1])
            print("Year Level:", LOBRES_student[2])
            print()

            found = True

    if not found:
        print("\nNo Students Found!")

    again = input("Do you want to search again? (YES/NO): ")

    if again.lower() != "yes":
        print("\nThank You!")
        break