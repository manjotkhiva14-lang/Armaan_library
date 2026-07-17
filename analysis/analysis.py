
import pandas as pd
import matplotlib.pyplot as plt

class Dashboard:
    def load_data(self):
        self.df = pd.read_csv("students_full.csv")
        self.df["seat_allotted"] = self.df["seat_allotted"].astype("Int64")

    def search_student(self):

        name = input("Enter the name of the student you want to search").lower()

        st = self.df[self.df["name"].str.lower() == name ]
        if st.empty:
            print("Student not found")
            return
        print(st)
    
    
    def generate_summary(self):
        self.summary = self.df.groupby("shift").agg({
            "student_id" : "count",
            "seat_allotted" : "count"
            })
        self.summary["efficiency"] = (self.summary["seat_allotted"] / self.summary["student_id"])*100
        self.summary["seat_status"] = self.summary["efficiency"].apply(
            lambda x:
            "full" if x == 100
            else "Pending" if x == 0
            else "Partial"
            )
        

    def show_insights(self):
        print("\n INSIGHTS")
        
        print("\n Best performing shift")
        best = self.summary["efficiency"].idxmax()
        print(best)
        
        print("\n Pending students")
        pending = self.df[self.df["seat_allotted"].isna()]
        print(pending)
        
        print("\n Occupancy")
        occ = self.df["seat_allotted"].notna().sum()
        print((occ/110)*100)
        
        print("\n Total allocatted students")
        tlt = self.df["seat_allotted"].notna().sum()
        print(tlt)


    def create_graphs(self):
        self.summary["seat_allotted"].plot(kind= "bar")
        plt.title("Allocated seats")
        plt.show()


        self.summary["seat_allotted"].plot(kind= "pie")
        plt.title("Allocated seats")
        plt.show()

        print(self.summary)

    def search_id(self):
        while True:
            try:
                student_id = int(input("Enter the id of the student you want to search"))
                if student_id <= 0:
                    print("invalid int ")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")
        sm = self.df[self.df["student_id"] == student_id ]
        if sm.empty:
            print("Student id not found")
            return
        print(sm)

    def delete_student(self):
        while True:
            try:
                student_id = int(input("Enter the id of the student you want to search"))
                if student_id <= 0:
                    print("invalid int ")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")
        
        ht = self.df[self.df ["student_id"] == student_id]
        
        if ht.empty:
            print("Student not found")
            return
        
        self.df = self.df.drop(ht.index)
        
        print("Student deleted successfully")

    def total_students(self):
        print(len(self.df))

    def show_shift_students(self):
        print("Available shifts")
        print("9-2")
        print("2-7")
        print("9-7")

        shift = input("Enter the shift").strip()
        sh = self.df[self.df["shift"] == shift]
        if sh.empty:
            print("Shift not found")
            return
        print(sh)

    def save_data(self):
        self.df.to_csv("students_full.csv" , index = False)


    def export_report(self):
        self.summary = self.summary.reset_index()
        self.summary.to_csv("dashboard_repot.csv" , index= False )