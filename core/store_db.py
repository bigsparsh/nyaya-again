from firebase_admin import firestore
from .firebase_config import *

fire_db = firestore.client()


def insert_into_user(email, name, phone, address, aadhar_id):
    lawyers = fire_db.collection("User").get()
    last_user_id = int(lawyers[-1].id)
    user_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address,
        'aadhar_id': aadhar_id,
        'cases': []
    }
    fire_db.collection("User").document(str(last_user_id + 1)).set(user_data)


def insert_into_lawyer(email, name, phone, address, bar_id, info, expertise):
    lawyers = fire_db.collection("Lawyers").get()
    last_lawyer_id = int(lawyers[-1].id)
    lawyer_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address,
        'bar_id': bar_id,
        'info': info,
        'expertise': expertise,
        'rating': 0,
        'cases': []
    }
    fire_db.collection("Lawyers").document(str(last_lawyer_id + 1)).set(lawyer_data)


def find_user(email):
    user = fire_db.collection("User").where("email", "==", email)
    user_info = user.get()[0].to_dict()
    return user_info


def find_lawyer(email):
    lawyer = fire_db.collection("Lawyers").where("email", "==", email)
    lawyer_info = lawyer.get()[0].to_dict()
    return lawyer_info


def list_lawyers():
    return [lawyer.to_dict() for lawyer in fire_db.collection("Lawyers").get()]


def list_users():
    return [user.to_dict() for user in fire_db.collection("User").get()]


def list_queries():
    return [query.to_dict() for query in fire_db.collection("Queries").get()]


def user_type(email):
    client = None
    try:
        find_lawyer(email)
        client = "lawyer"
    except Exception as _:
        pass
    try:
        find_user(email)
        client = "user"
    except Exception as _:
        pass

    return client

