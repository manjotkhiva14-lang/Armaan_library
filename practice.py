import pandas as pd 

df = pd.read_csv("students_full.csv")

print(df)
print(df.columns)

print(df ["shift"].value_counts())

print(df[df["seat_allotted"].isna()])

print(df[df["seat_allotted"].notna()])


occupied = df["seat_allotted"].notna().sum()

percentage = (occupied/110)*100

print(percentage)

df["shift_type"] = df["shift"].apply(lambda x : "full day" if x == "9-7" else "half day")

print(df)

srt = df.sort_values(by = "seat_allotted" , ascending=False)
print(srt)

summary = df.groupby("shift").agg({
    "student_id" : "count",
    "seat_allotted" : "count"
})
summary["efficiency"] = (summary["seat_allotted"] / summary["student_id"]) * 100
summary["efficiency"] = summary["efficiency"].round(2)
print(summary)
 