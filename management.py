from students import Student
from seats import Seat
import json
import pandas as pd
class Management:
    def __init__(self):
        self.students = {}
        self.seats = {}

        for i in range(1,111):
            seat = Seat(i)
            self.seats[i] = seat
        
        
        self.shifts = {
            1 : "9-2",
            2 : "2-7",  
            3 : "9-7"
        }
        
    
    def get_valid_int(self,prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("invalid input")
                    continue
                return value
            except ValueError:
                print("Please enter the valid input")

    def get_valid_string(self,prompt):
        while True:
                value = input(prompt).strip()
                if value == "":
                    print("Value cannot be empty")
                    continue
                return value
            
    
    def get_shift(self):
        while True:
            print("\n Available shifts:")
            for key , value in self.shifts.items():
                print(f"{key} : {value}")

            choice = self.get_valid_int("Select shift:")

            if choice in self.shifts:
                return self.shifts[choice]
            
            print("Invalid choice, try again")

    def add_student(self):
        name = self.get_valid_string("Enter the name of the student")
        while True:
            student_id = self.get_valid_int("Enter the id of the student")
            if student_id in self.students:
                print("This id is not available . Use another")
                continue
            break
        contact = self.get_valid_string("Enter the contact no. of the student")
        shift = self.get_shift()

        student = Student(name,student_id,contact,shift)
        self.students[student.student_id] = student
    
    def allot_seat(self):
        studentid = self.get_valid_int("Enter the id of the student")
        st = self.students.get(studentid)
        if st is None:
            print("Student not found")
            return 
        if st.seat_allotted is not None:
            print("Student already has a seat")
            return
        shift = st.shift
        for seat in self.seats.values():
            if shift == "9-7":
                if seat.allotted_to["9-2"] is not None or seat.allotted_to["2-7"] is not None:
                    continue
            if shift in ["9-2" , "2-7"]:
                if seat.allotted_to["9-7"] is not None:
                    continue
            if seat.allotted_to[shift] is None:
                seat.allotted_to[shift] = st.student_id
                st.seat_allotted = seat.seat_number
     
                print(f" Seat number : {seat.seat_number} is allotted for {shift} to {st.name}")
                return
        print("No seats available for this shift")
    
    def unallot_seat(self):
        student_id = self.get_valid_int("Enter the id of the student")
        st = self.students.get(student_id)
        
        if st is None:
            print("Student not found")
            return
        
        if st.seat_allotted is None:
            print("Student didnt have any seat")
            return
        
        shift = st.shift
        
        seat = self.seats.get(st.seat_allotted)
        if seat is None:
            print("Seat data error")
            return
        
        seat.allotted_to[shift] = None
        st.seat_allotted = None
      
        
        print("Seat unallotted successfully")
        
    
    def check_seat(self):
        seat_number = self.get_valid_int("Enter the number of the seat you want to check")
        
        seat = self.seats.get(seat_number)
        
        if seat is None:
            print("Seat not found")
            return
        
        print(f"Seat number = {seat.seat_number} status:")
        
        is_empty = True
        for shift , student_id in seat.allotted_to.items():
            print(f"\n Shift {shift}:")

            if student_id is not None:
                is_empty = False
                st = self.students.get(student_id)
                
                if st :
                    print(f" Student name : {st.name}")
                    print(f" Student id : {st.student_id}")
                    print(f" Student contact : {st.contact}")
                else:
                    print("Student data not found")
        if is_empty:
            print("Seat is empty")

    def check_student(self):
        if not self.students:
            print("Students list is empty")
            return
        student_id = self.get_valid_int("Enter the id of the student")
        st = self.students.get(student_id)
        if st:
            print(f" Student name : {st.name}")
            print(f" Student id : {st.student_id}")
            print(f" Student contact : {st.contact}")
            print(f" Shift time : {st.shift}")
            print(f" Seat alloted : {st.seat_allotted}")
        else:
            print("Student not found")

    def search_by_name(self):
        name = input("Enter the name of the student you want to search").strip()
        found = False
        for student in self.students.values():
            if name == student.name:
                found = True
    
                print(f" Student name : {student.name}")
                print(f" Student id : {student.student_id}")
                print(f" Student contact : {student.contact}")
                print(f" Shift time : {student.shift}")
                print(f" Seat alloted : {student.seat_allotted}")
        if not found:
            print("Student not found")

                
    def save_students(self):
        data = []
        for student in self.students.values():
            data.append({
                "name" : student.name,
                "student_id" : student.student_id,
                "contact" : student.contact,
                "shift" : student.shift,
                "seat_allotted" : student.seat_allotted                
            })
        with open("students.json" , "w")as file:
            json.dump(data,file,indent =4) 
        print("Student saved successfully")
    
    def load_students(self):
        try:
            with open("students.json" , "r")as file:
                data = json.load(file) 

            for s in data:
                student = Student(s["name"] , s["student_id"] , s["contact"] , s["shift"] )
                student.seat_allotted = s["seat_allotted"]
                self.students[student.student_id] = student
            print("Students loaded successfully")
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("File is empty")

    def save_seats(self):
        seat_data = []
        for seat in self.seats.values():
            seat_data.append({
                "seat_number" : seat.seat_number,
                "allotted_to" : seat.allotted_to
            })
        with open("seats.json" , "w")as file:
            json.dump(seat_data,file, indent = 4) 
        print("Seat saved successfully")
    def load_seats(self):
        try:
            with open("seats.json" , "r")as file:
                user_data = json.load(file) 

            for b in user_data:
                seat = Seat(b["seat_number"])
                seat.allotted_to = b["allotted_to"]
                self.seats[seat.seat_number] = seat
            print("Seats loaded successfully")
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("File is empty")

    def load_students_from_csv(self):
        try:
            df = pd.read_csv("students_full.csv")

            for _, row in df.iterrows():
                student = Student(
                    row["name"],
                    int(row["student_id"]),
                    str(row["contact"]),
                    row["shift"]
                )

                if pd.notna(row["seat_allotted"]):
                    student.seat_allotted = int(row["seat_allotted"])
                else:
                    student.seat_allotted = None

                self.students[student.student_id] = student

            print("Students loaded from csv successfully")

        except FileNotFoundError:
            print("csv file not found")

    def export_students_to_csv(self):
        data = []

        for student in self.students.values():
            data.append({
                "name" : student.name,
                "student_id" : student.student_id,
                "contact" : student.contact,
                "shift" : student.shift,
                "seat_allotted" : student.seat_allotted
            })

        df = pd.DataFrame(data)

        df.to_csv("students_full.csv" , index = False)

        print("Students exported in CSV successfully")
    



    


