# import pandas as pd

# df = pd.read_csv("students_full.csv")
# print(df)

# print(df.columns)

# df["seat_allotted"] = df["seat_allotted"].astype("Int64")

# print(df.info())

# print("\n Students per shift:")
# print(df["shift"].value_counts())

# print("\n Students without seat:")
# print(df[df["seat_allotted"].isna()])

# print("\n Count of students without seats:")
# print(df["seat_allotted"].isna().sum())

# print("\n Students without seat in (9-2) shift")
# result = df[(df["shift"] == "9-2") & (df["seat_allotted"].isna())]
# print(result)
# print("\n Count:" , len(result))

# import matplotlib.pyplot as plt

# df["shift"].value_counts().plot(kind="bar")
# plt.title("Students per shift")
# plt.show()

# print("\n Students who already have seats")
# print(df[df["seat_allotted"].notna()])

# print("\n Total allocatted students")
# print(df["seat_allotted"].notna().sum())

# print("\n Percentage of students who got seats")
# percentage = df["seat_allotted"].notna().mean()*100
# print(percentage)

# print("\n shift with maximum students ")
# print(df["shift"].value_counts().idxmax())

# print("\n allocated students in each shift")
# sm = df[df["seat_allotted"].notna()]
# print(sm["shift"].value_counts())

# print("\n Students in each shift without seat")
# wt = df[df["seat_allotted"].isna()]
# print(wt["shift"].value_counts())

# print("\n Adding a new column")
# df["shift_type"] = df["shift"].apply(lambda x: "full day" if x == "9-7" else "half day")
# print(df)

# print("\n All students with seat number greater than one")
# yt = df[df["seat_allotted"]>1]
# print(yt)

# print("\n Sorting students by seat number")
# srt = df.sort_values(by = "seat_allotted")
# print(srt)

# import matplotlib.pyplot as plt
# df["shift"].value_counts().plot(kind = "pie")
# plt.title("shift distribution")
# plt.show()

# print("\n Percentage of occupied seats")
# occupied = df["seat_allotted"].notna().sum()
# percentage =(occupied /110 ) *100
# print(percentage)

# import pandas as pd
# import matplotlib.pyplot as plt 

# df = pd.read_csv("students_full.csv")
# print(df)

# print(df.groupby("shift")["seat_allotted"].count())

# print(df.groupby("shift")["student_id"].count())

# allocatted = df.groupby("shift")["seat_allotted"].count()
# total = df.groupby("shift")["student_id"].count()
# eff =( allocatted / total) *100
# print(eff)


# summary = df.groupby("shift").agg({
#     "student_id" : "count",
#     "seat_allotted" : "count",
#     })
# summary["efficiency"] = (summary["seat_allotted"] / summary["student_id"] ) * 100 
# print(summary)

# summary.columns = ["Total Students" , "Allocated seats" , "Efficiency"]
# summary["Efficiency"]= summary["Efficiency"].round(2)
# print(summary)

# summary["Allocated seats"].plot(kind= "bar")
# plt.title("Allocated seats")
# plt.show()


# best = summary["Efficiency"].idxmax()
# print(best)


# summary = summary.reset_index()
# summary.to_csv("summary_report.csv" , index = False)

# summary["seat_status"] = summary["Efficiency"].apply(
#     lambda x:
#     "Full" if x == 100
#     else "Pending" if x == 0
#     else "Partial"
# )
# print(summary)

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