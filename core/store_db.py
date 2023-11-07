from firebase_admin import firestore
from .firebase_config import *
import json

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
        'cases': [],
        'queries': []
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
        'cases': [],
        'queries': []
    }
    fire_db.collection("Lawyers").document(str(last_lawyer_id + 1)).set(lawyer_data)


def find_user_by_email(email):
    user = fire_db.collection("User").where("email", "==", email)
    user_info = user.get()[0].to_dict()
    user_info["user_id"] = user.get()[0].id
    return user_info


def find_lawyer_by_email(email):
    lawyer_local = fire_db.collection("Lawyers").where("email", "==", email)
    lawyer_info = lawyer_local.get()[0].to_dict()
    for index, query in enumerate(lawyer_info["queries"]):
        lawyer_info["queries"][index] = find_query_by_id(query.id)
    return lawyer_info


def find_lawyer_by_id(lawyer_id):
    lawyer = fire_db.collection("Lawyers").document(lawyer_id).get().to_dict()
    lawyer["lawyer_id"] = lawyer_id
    return lawyer


def find_query_by_id(query_id):
    query = fire_db.collection("Queries").document(query_id).get().to_dict()
    query["query_id"] = query_id
    query["user"] = query["user_id"].get().to_dict()
    query["user"]["user_id"] = query["user_id"].id
    query.pop("user_id")
    return query


def list_lawyers():
    lawyers = []
    for index, lawyer in enumerate(fire_db.collection("Lawyers").get()):
        lawyers.append(lawyer.to_dict())
        lawyers[index]["lawyer_id"] = lawyer.id
    return lawyers


def list_users():
    users = []
    for index, user in enumerate(fire_db.collection("User").get()):
        users.append(user.to_dict())
        users[index]["user_id"] = user.id
    return users


def list_queries(lawyer_local):
    qry_lst = []
    lawyer_accepted_queries = [query["query_id"] for query in lawyer_local["queries"]]
    queries_id = [query.id for query in fire_db.collection("Queries").get()]
    queries_id = [x for x in queries_id if x not in lawyer_accepted_queries]
    for query_id in queries_id:
        qry_lst.append(find_query_by_id(query_id))
    return qry_lst


def accept_query(lawyer_local, query_local):
    lawyer_accepted_queries = [query["query_id"] for query in lawyer_local["queries"]]
    qry_lst = []
    for query_id in lawyer_accepted_queries:
        qry_lst.append(fire_db.collection("Queries").document(query_id))
    qry_lst.append(fire_db.collection("Queries").document(query_local["query_id"]))
    lawyer_local["queries"] = qry_lst
    fire_db.collection("Lawyers").document(lawyer_local["lawyer_id"]).set(lawyer_local, merge=True)


def user_type(email):
    client = None
    try:
        find_lawyer_by_email(email)
        client = "lawyer"
    except Exception as _:
        pass
    try:
        find_user_by_email(email)
        client = "user"
    except Exception as _:
        pass

    return client


def make_query(email, title, description):
    user = find_user_by_email(email)
    queries = fire_db.collection("Queries").get()
    last_query_id = int(queries[-1].id)
    query_data = {
        "title": title,
        "description": description,
        "user_id": fire_db.collection("User").document(user["user_id"]),
        "accepted": False
    }
    fire_db.collection("Queries").document(str(last_query_id + 1)).set(query_data)


def update_user(email):
    user = find_user_by_email(email)
    user_id = user["user_id"]
    user.pop("user_id")


def update_lawyer(email):
    lawyer = find_user_by_email(email)
    lawyer_id = lawyer["lawyer_id"]
    lawyer.pop("user_id")

