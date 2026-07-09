from analysis import Dashboard
dash = Dashboard()
dash.load_data()
dash.generate_summary()
 
while True:
    print("\n Menu system")
    print("0. search student")
    print("1. show insights")
    print("2. create graphs")
    print("3. student_id")
    print("4. delete student")
    print("5. total students")
    print("6. show particular shift students")
    print("7. export report")
    print("8. exit")

    i = input("enter the choice")

    if i == "0":
        dash.search_student()

    elif i == "1":
        dash.show_insights()

    elif i =="2":
        dash.create_graphs()
    
    elif i == "3":
        dash.search_id()

    elif i == "4":
        dash.delete_student()
        dash.save_data()

    elif i == "5":
        dash.total_students()
    
    elif i == "6":
        dash.show_shift_students()

    elif i == "7":
        dash.export_report()
        print("Report exported")
        
    elif i == "8":
        print("Program exited")
        break
    
    else:
        print("invalid choice")