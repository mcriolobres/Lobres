LOBRES_salary = {"E104": {
    "EmpName" : "Kobe Bryant",
    "DailyHrs" : [8, 9, 8.5, 10, 8]
    },
    "E601": {
        "EmpName" :"Allen Iverson",
        "DailyHrs" : [9,10,8,8,9]
    }
}
LOBRES_weeklybasic = 9000
LOBRES_rateperhour = LOBRES_weeklybasic / 40


LOBRES_EmpID = input("Enter Employee ID: ")

if LOBRES_EmpID not in LOBRES_salary:
    print("Not Found")

else:
    LOBRES_employee = LOBRES_salary[LOBRES_EmpID]
    print("Employee Name: ",
    LOBRES_employee["EmpName"])
    print("Daily Hours: ", end="")

    for hours in LOBRES_employee["DailyHrs"]:
        print(hours, end=" ")

    print()

    LOBRES_totalhours = sum(LOBRES_employee["DailyHrs"])
    LOBRES_excess = LOBRES_totalhours - 40

    # Calculate overtime and gross pay
    LOBRES_overtime = LOBRES_excess * LOBRES_rateperhour * 1.5
    LOBRES_grosspay = LOBRES_weeklybasic + LOBRES_overtime

    print("Excess hours:", LOBRES_excess)
    print("Rate per hour:", LOBRES_rateperhour)
    print("Overtime:", LOBRES_overtime)
    print("Weekly Basic:", LOBRES_weeklybasic)
    print("GrossPay:", LOBRES_grosspay)
