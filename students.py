class Student:
    def __init__ (self, name, student_id, contact, shift = None):
        self.name = name
        self.student_id = student_id
        self.contact = contact
        self.shift = shift     
        self.seat_allotted = None