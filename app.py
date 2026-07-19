from flask import Flask, render_template, request, redirect, url_for
from library.management import Management
from library.students import Student

man = Management()
man.load_students()
man.load_seats()

app = Flask(__name__)

@app.route("/")
def home():
    total_students = len(man.students)
    occupied_seats = sum(1 for s in man.students.values() if s.seat_allotted is not None)
    total_seats = len(man.seats)
    available_seats = total_seats - occupied_seats

    shift_counts = {"9-2": 0, "2-7": 0, "9-7": 0}
    for s in man.students.values():
        if s.shift in shift_counts:
            shift_counts[s.shift] += 1

    return render_template("home.html",
        library_name="Armaan Library",
        total_students=total_students,
        total_seats=total_seats,
        occupied_seats=occupied_seats,
        available_seats=available_seats,
        shift_counts=shift_counts
    )


@app.route("/students")
def students():
    student_list = list(man.students.values())
    return render_template("students.html", students=student_list)


@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]

        try:
            student_id = int(request.form["student_id"])
        except ValueError:
            return render_template("add_student.html", error="Please enter a valid student ID")

        if student_id in man.students:
            return render_template("add_student.html", error="This ID is already taken")

        contact = request.form["contact"]
        shift = request.form["shift"]

        student = Student(name, student_id, contact, shift)
        man.students[student_id] = student
        man.save_students()

        return render_template("add_student.html", message=f"{name} added successfully")
    return render_template("add_student.html")


@app.route("/manage-seat", methods=["GET", "POST"])
def manage_seat():
    if request.method == "POST":
        action = request.form["action"]
        student_id = int(request.form["student_id"])
        if action == "allot":
            message = man.allot_seat_web(student_id)
        else:
            message = man.unallot_seat_web(student_id)
        return render_template("manage_seat.html", message=message, active_tab=action)
    return render_template("manage_seat.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "POST":
        check_type = request.form["check_type"]
        if check_type == "seat":
            seat_number = int(request.form["seat_number"])
            message = man.check_seat_web(seat_number)
            return render_template("check_seat_result.html", message=message, seat_number=seat_number)
        else:
            student_id = int(request.form["student_id"])
            message = man.check_student_web(student_id)
            return render_template("check_student_result.html", message=message)
    return render_template("check.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)