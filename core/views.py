from django.shortcuts import render, redirect
from .fire_auth import User, Lawyer
from .store_db import *
from .mail_sendificator import send_email_to

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
    try:
        if request.session["user"]:
            return redirect(dashboard)
        else:
            raise KeyError
    except KeyError as _:
        return render(request, "home.html")


def user_register(request):
    try:
        if request.session["user"]:
            return redirect(dashboard)
        else:
            raise KeyError
    except KeyError as _:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            aadhar_id = request.POST['aadhar']
            phone = request.POST['phone']
            password = request.POST['password']
            User(email=email, password=password).create(name=name, address=address, aadhar_id=aadhar_id,
                                                        phone=phone)
            message = ("This is to inform you that you have successfully created a Nyaya-Mitra account and you can "
                       "login to access the dashboard. \nIt is lovely to see that you have choosen to give our "
                       "services a chance, we hope your nyaya-mitra makes your problems go away.")
            send_email_to("Welcome to the Nyaya-Mitra family", name, message, email)
            return redirect(login)
        else:
            return render(request, "user_register.html")


def lawyer_register(request):
    try:
        if request.session["user"]:
            return redirect(dashboard)
        else:
            raise KeyError
    except KeyError as _:
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
    try:
        if request.session["user"]:
            return redirect(dashboard)
        else:
            raise KeyError
    except KeyError as _:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            if user_type(email) == "lawyer":
                client = Lawyer(email=email, password=password).authenticate()
            if user_type(email) == "user":
                client = User(email=email, password=password).authenticate()
            request.session["user"] = client
            return redirect(dashboard)
        else:
            return render(request, "login.html")


def query_generator(request):
    try:
        if request.session["user"] and user_type(request.session["user"]["email"]) == "user":
            if request.method == "POST":
                title = request.POST["title"]
                description = request.POST["description"]
                make_query(request.session["user"]["email"], title, description)
                return redirect(dashboard)
            else:
                return render(request, "query_generator.html")
        else:
            raise KeyError
    except KeyError as _:
        return redirect(login)


def clear_buffer(request):
    request.session["buffer"] = None
    return redirect(dashboard)


def dashboard(request):
    try:
        if request.session["user"]:
            client_email = request.session["user"]["email"]
            if user_type(client_email) == "user":
                main_info = list_lawyers()
            if user_type(client_email) == "lawyer":
                main_info = list_queries(request.session["user"])
            if request.method == "POST":
                all_keys = list(request.POST.keys())
                request_key = all_keys[1]
                if user_type(client_email) == "user":
                    request.session["buffer"] = find_lawyer_by_id(request_key)
                if user_type(client_email) == "lawyer":
                    request.session["buffer"] = find_query_by_id(request_key)
                return redirect(info_page)

            try:
                if request.session["buffer"]:
                    return redirect(info_page)
            except KeyError as _:
                pass

            print(main_info)

            return render(request, "dashboard.html",
                              {"type": user_type(request.session["user"]["email"]),
                               "user": request.session["user"],
                               "main_info": main_info})
        else:
            raise KeyError
    except KeyError as _:
        return redirect(login)


def info_page(request):
    try:
        if request.session["user"] and request.session["buffer"]:
            client_email = request.session["user"]["email"]
            return render(request,
                          "info_page.html",
                          {"data": request.session["buffer"],
                           "client_type": user_type(client_email)})
        else:
            raise KeyError
    except Exception as _:
        return redirect(login)


def query_accept(request):
    try:
        client_email = request.session["user"]["email"]
        if request.session["user"] and request.session["buffer"] and user_type(client_email) == "lawyer":
            accept_query(request.session["user"], request.session["buffer"])
            message = (f"You put out a query titled '{request.session['buffer']['title']}'."
                       f"\nIt look like one of our legal representative Advocate {request.session['user']['name']} "
                       f"has accepted your legal query and you can communicate with them to ensure your satisfaction "
                       f"or you could wait for other lawyers to accept your query and then you can select one of those"
                       f" lawyers to be your legal helper.\n - Nyaya Mitra team")
            send_email_to("Your query was accepted by a lawyer!",
                          request.session["buffer"]["user"]["name"],
                          message,
                          request.session["buffer"]["user"]["email"])
            request.session["user"] = find_lawyer_by_email(client_email)
            return redirect(clear_buffer)
    except KeyError as _:
        return redirect(info_page)


def logout(request):
    request.session["user"] = None
    return redirect(home)
