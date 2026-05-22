from management import Management
man = Management()
man.load_students()
man.load_seats()
man.load_students_from_csv()
man.save_students()
while True:
    print(" *****ARMAAN LIBRARY***** ")
    print("1. add student")
    print("2. allot_seat")
    print("3. unallot seat")
    print("4. check seat")
    print("5. check student")
    print("6. exit")

    i = input("Enter the choice")
    

    if i == "1":
        man.add_student()
        man.save_students()
    elif i == "2":
        man.allot_seat()
        man.save_students()
        man.save_seats()
    elif i == "3":
        man.unallot_seat()
        man.save_students()
        man.save_seats()
    elif i == "4":
        man.check_seat()
    elif i == "5":
        man.check_student()
    elif i == "6":
        man.export_students_to_csv()
        print("Program exited")
        break
    else:
        print("Enter the valid input")