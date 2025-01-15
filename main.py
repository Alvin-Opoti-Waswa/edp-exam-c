class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class BooksApplicationSentEvent(Event):
    def __init__(self, student_id_number, date):
        super().__init__("application_sent_request", {"student_id_number": student_id_number, "date": date})

class BooksApplicationrejectedEvent(Event):
    def __init__(self, student_id_number, is_confirmed):
        super().__init__("application_confirmation", {"student_id_number": student_id_number, "is_confirmed": is_confirmed})

event_queue = []


class Student:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number, school_year):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.school_year = school_year

         def ask_for_book_application_appointment(self, date):
        event = ApplicationSentEvent(self.admission_number, date)
        event_queue.append(event)
        print('application', event.name, 'sent!')

class University:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email


    def handle_application_request(self, event):
        print(f"Received appointment request for Books: {event.payload['student_id_number']} on {event.payload['date']}")
        confirmation_event = BooksApplicationSentEvent(event.payload["student_id_number"], is_confirmed=True)
        event_queue.append(confirmation_event)
        print('application', confirmation_event.name, 'done!')


# Code Usage
alvin = Student("alvin", "Opoti", '7.02.2022', 'Nairobi', '234578645', '34461')
marcus = Student("marcus", "farah", '9.02.2024', 'Nairobi', '456783987', '89991')
daniel = Student("daniel", "ole", '14.02.2020', 'Nairobi', '253874659', '23441')

alvin.ask_for_emask_for_book_application_appointmentbassy_appointment('20.12.2024')
marcus.ask_for_book_application_appointment('21.12.2024')
daniel.ask_for_book_application_appointment('22.12.2024')

University_of_Technology_and_Arts = University('UTA', 'Warsaw, Ols 12', '234678987', 'uts@edu.tr')