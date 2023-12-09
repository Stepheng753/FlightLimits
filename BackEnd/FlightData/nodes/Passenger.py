

class Passenger:

    def __init__(self, id, type, age=None, family_name=None, given_name=None, title=None, dob=None, gender=None, phone_number=None, email=None, infant_passenger_id=None) -> None:
        self.id = id
        self.type = type
        self.age = age
        self.family_name = family_name
        self.given_name = given_name
        self.title = title
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.infant_passenger_id = infant_passenger_id

    def set_age(self, age):
        self.age = age

    def set_family_name(self, family_name):
        self.family_name = family_name

    def set_given_name(self, given_name):
        self.given_name = given_name

    def set_title(self, title):
        self.title = title

    def set_dob(self, dob):
        self.dob = dob

    def set_gender(self, gender):
        self.gender = gender

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def set_infant_passenger_id(self, infant_passenger_id):
        self.infant_passenger_id = infant_passenger_id

    def to_dict(self):
        return {
            "id": self.id,
            "family_name": self.family_name,
            "given_name": self.given_name,
            "title": self.title,
            "born_on": self.dob,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "email": self.email,
            "infant_passenger_id" : self.infant_passenger_id
        }

    def __str__(self) -> str:
        rtnStr = "Type: " + self.type + "\n"
        rtnStr += "Name: " + self.title + " " + self.given_name + " " + self.family_name + "\n"
        rtnStr += "Date of Birth: " + self.dob + "\n"
        rtnStr += "Gender: " + self.gender + "\n"
        rtnStr += "Contact: " + self.phone_number + " :: " + self.email
        return rtnStr
