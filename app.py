from flask import Flask , render_template , request , redirect , url_for
from management import Management
from students import Student
man = Management()
man.load_students()
man.load_seats()

app = Flask(__name__)

@app.route("/")
def home():
    total_students = len(man.students)
    total_seats = len(man.seats)
    return render_template("home.html",library_name = "Armaan Library" , 
                           total_students = total_students,
                           total_seats = total_seats)

@app.route("/students")
def students():
    student_list = list(man.students.values())
    return render_template("students.html" , students = student_list)

@app.route("/add-student" , methods=["GET" , "POST"])
def add_student():
    if request.method == "POST":
        name = request.form ["name"]
        try:
            student_id = int(request.form["student_id"])
        except ValueError:
            return render_template("add_student.html" , error = "please enter the valid student id")
        contact = request.form["contact"]
        shift = request.form["shift"]
        student = Student(name,student_id,contact,shift)
        man.students[student_id] = student 
        man.save_students()
        return redirect (url_for("students"))   
    return render_template("add_student.html")

@app.route("/allot-seat" , methods =["GET" , "POST"])
def allot_seat():
    if request.method == "POST":
        student_id = int(request.form["student_id"])
        message = man.allot_seat_web(student_id)
        return message
    return render_template("allot_seat.html")

@app.route("/unallot-seat" , methods = ["GET"  , "POST" ])
def unallot_seat():
    if request.method == "POST":
        student_id = int(request.form["student_id"])
        message = man.unallot_seat_web(student_id)
        return message
    return render_template("unallot_seat.html")

@app.route("/check-seat" , methods = ["GET" ,  "POST"])
def check_seat():
    if request.method == "POST":
        seat_number = int(request.form["seat_number"])
        message = man.check_seat_web(seat_number)
        return message
    return render_template("check_seat.h")

@app.route("/check-student" , methods = ["GET" , "POST"])
def check_student():
    if request.method == "POST":
        student_id = int(request.form["student_id"])
        message = man.check_student_web(student_id)
        return message
    return render_template("check_student.html")

@app.route("/search-student" , methods = ["GET" , "POST"])
def search_by_name_web():
    if request.method == "POST":
        name = str(request.form["name"].strip().lower())
        message = man.search_by_name_web(name)
        return message
    return render_template("search_student.html")


@app.route("/about")
def about():
    return "<h1>Armaan Library</h1><p>A seat management system</p>"

if __name__ == "__main__":
    app.run(debug=True)