from django.shortcuts import render, redirect
from .fire_auth import User, Lawyer
from .store_db import list_lawyers, user_type, make_query, list_queries

expertise = {
    "Criminal Defense": None,
    "Family": None,
    "Personal Injury": None,
    "Estate Planning": None,
    "Bankruptcy": None,
    "Real Estate": None,
    "Intellectual Property": None,
    "Corporate": None,
    "Employment": None,
    "Immigration": None,
}


def home(request):
    if request.session["user"]:
        return redirect(dashboard)
    else:
        return render(request, "home.html")


def user_register(request):
    if request.session["user"]:
        return redirect(dashboard)
    else:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            aadhar_id = request.POST['aadhar']
            phone = request.POST['phone']
            password = request.POST['password']
            User(email=email, password=password).create(name=name, address=address, aadhar_id=aadhar_id, phone=phone)
            return redirect(login)
        else:
            return render(request, "user_register.html")


def lawyer_register(request):
    if request.session["user"]:
        return redirect(dashboard)
    else:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            bar_id = request.POST['bar']
            info = request.POST['info']
            phone = request.POST['phone']
            password = request.POST['password']
            expertise_list = []

            for exp in list(expertise.keys()):
                try:
                    if request.POST[exp] == "on":
                        expertise_list.append(exp)
                except Exception as _:
                    pass

            Lawyer(email, password).create(name, phone, address, bar_id, info, expertise_list)
            return redirect(login)
        else:
            return render(request, "lawyer_register.html",
                          {'expertise_categories': list(expertise.keys())})


def login(request):
    if request.session["user"]:
        return redirect(dashboard)
    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            print(user_type(email))
            if user_type(email) == "lawyer":
                client = Lawyer(email=email, password=password).authenticate()
            if user_type(email) == "user":
                client = User(email=email, password=password).authenticate()
            request.session["user"] = client
            return redirect(dashboard)

        else:
            return render(request, "login.html")


def query_generator(request):
    if request.session["user"] and user_type(request.session["user"]["email"]) == "user":
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            make_query(request.session["user"]["email"], title, description)
            return redirect(dashboard)
        else:
            return render(request, "query_generator.html")
    else:
        return redirect(login)


def dashboard(request):
    if request.session["user"]:
        client_type = request.session["user"]["email"]
        if request.method == "POST":
            print(request.POST)

        # else:
        if user_type(client_type) == "user":
            main_info = list_lawyers()
        if user_type(client_type) == "lawyer":
            main_info = list_queries()
        return render(request, "dashboard.html",
                      {"type": user_type(request.session["user"]["email"]),
                       "user": request.session["user"],
                       "main_info": main_info})
    else:
        return redirect(login)


def logout(request):
    request.session["user"] = None
    return redirect(home)
