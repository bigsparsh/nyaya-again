import pyrebase as pb
from .store_db import insert_into_user, insert_into_lawyer, find_user, find_lawyer

firebaseConfig = {
    'apiKey': "AIzaSyC9Su0Qp87w52JnFegOQJLPNAC5qmNepik",
    'authDomain': "bigproject-d6846.firebaseapp.com",
    'databaseURL': "https://bigproject-d6846-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "bigproject-d6846",
    'storageBucket': "bigproject-d6846.appspot.com",
    'messagingSenderId': "962134580824",
    'appId': "1:962134580824:web:87e73c1b8dd970f9af742d",
    'measurementId': "G-L6ZXTYCE66"
}

fb = pb.initialize_app(firebaseConfig)
aut = fb.auth()


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def authenticate(self):
        user = aut.sign_in_with_email_and_password(self.email, self.password)
        return find_user(user["email"])

    def create(self, name, phone, address, aadhar_id):
        aut.create_user_with_email_and_password(self.email, self.password)
        insert_into_user(self.email, name, phone, address, aadhar_id)


class Lawyer:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def authenticate(self):
        lawyer = aut.sign_in_with_email_and_password(self.email, self.password)
        return find_lawyer(lawyer["email"])

    def create(self, name, phone, address, bar_id, info, expertise):
        aut.create_user_with_email_and_password(self.email, self.password)
        insert_into_lawyer(self.email, name, phone, address, bar_id, info, expertise)

