class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class ApplicationSentEvent(Event):
    def __init__(self, passport_number, date):
        super().__init__("application_sent_request", {"passport_number": passport_number, "date": date})

class ApplicationrejectedEvent(Event):
    def __init__(self, passport_number, is_confirmed):
        super().__init__("application_confirmation", {"passport_number": passport_number, "is_confirmed": is_confirmed})

event_queue = []


class Student:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number, admission_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.admission_number = admission_number

         def ask_for_application_appointment(self, date):
        event = ApplicationSentEvent(self.passport_number, date)
        event_queue.append(event)
        print('application', event.name, 'sent!')

class University:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email