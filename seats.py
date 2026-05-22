class Seat:
    def __init__ (self,seat_number):
        self.seat_number = seat_number
        self.allotted_to = {
            "9-2": None,
            "2-7": None,
            "9-7": None
        }
   