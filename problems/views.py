import os

from django import forms
from django.shortcuts import render
from .models import User, Item, CTFUser


class FlagForm(forms.Form):
    submitted_flag = forms.CharField(label="submitted_flag")


class Problem2LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")


class Problem4SearchForm(forms.Form):
    search_content = forms.CharField(label="search_content")


class Problem3SubmitForm(forms.Form):
    post_content = forms.CharField(label="post")


flags = {
    1: "<FLAG>easy_peasy<FLAG>",
    2: "<FLAG>ok_nice_work_with_sql<FLAG>",
    3: "<FLAG>so_you_found_the_login_cookie<FLAG>",
    4: "<FLAG>good_work_overflowing_the_balance_mate<FLAG>",
    5: "<FLAG>flag_good_work_figuring_this_one_out_flag<FLAG>"
}


def check_flag(request):
    if "submit_flag" in request.POST and (form := FlagForm(request.POST)).is_valid():
        flag = form.cleaned_data["submitted_flag"]
        current_problem = request.session["current_problem"]
        valid = "failure"
        if flag == flags[current_problem]:
            valid = "success"
            user = CTFUser.objects.get(email=request.session["username"])
            user.solved.append(current_problem)
            user.save()
            request.session["solved"] = list(user.solved)
        return flag, valid


def problem_1(request):
    assert request.session["username"]
    request.session["current_problem"] = 1
    if request.method == "POST":
        if check := check_flag(request):
            flag, valid = check
            return render(request, "problem_1.html", {
                "request": request,
                "flag": flag,
                "valid_flag": valid
            })
    return render(request, "problem_1.html", {
        "flag": "",
        "request": request,
        "valid_flag": ""
    })


def problem_2(request):
    assert request.session["username"]
    request.session["current_problem"] = 2
    error = ""
    if request.method == "POST":
        if check := check_flag(request):
            flag, valid = check
            return render(request, "problem_2.html", {
                "request": request,
                "flag": flag,
                "valid_flag": valid,
                "login": False,
                "error": error
            })
        elif "sql_injection_login" in request.POST and (form := Problem2LoginForm(request.POST)).is_valid():
            u, p = form.cleaned_data["username"], form.cleaned_data["password"]
            print(User.objects.all())
            if len(User.objects.raw(f"select * from problems_user where username='{u}' and password='{p}'")) == 1:
                return render(request, "problem_2.html", {
                    "username": request.session["username"],
                    "request": request,
                    "login": True,
                    "error": error
                })
            error = "Username or password is incorrect"
    return render(request, "problem_2.html", {
        "username": request.session["username"],
        "request": request,
        "login": False,
        "error": error
    })


# atrocious programming and logic
# too bad
def problem_3(request):
    assert request.session["username"]
    request.session["current_problem"] = 3
    response = None
    try:
        logged_in = request.COOKIES["logged_in"]
    except KeyError:
        logged_in = "False"
    if request.method == "POST":
        if check := check_flag(request):
            flag, valid = check
            response = render(request, "problem_3.html", {
                "request": request,
                "flag": flag,
                "valid_flag": valid,
                "posts": [],
                "error": "",
                "logged_in": logged_in
            })
        elif "cookie_jr_login" in request.POST and (Problem2LoginForm(request.POST)).is_valid():
            response = render(request, "problem_3.html", {
                "flag": "",
                "request": request,
                "valid_flag": "",
                "posts": [],
                "error": "Username or password is incorrect",
                "logged_in": logged_in
            })
    else:
        response = render(request, "problem_3.html", {
            "flag": "",
            "request": request,
            "valid_flag": "",
            "posts": [],
            "error": "",
            "logged_in": logged_in
        })
    # if cookie logged_in is not set
    if logged_in == "False":
        response.set_cookie("logged_in", False)
    return response


def problem_4(request):
    assert request.session["username"]
    request.session["current_problem"] = 4
    if request.method == "POST":
        if check := check_flag(request):
            flag, valid = check
            return render(request, "problem_4.html", {
                "request": request,
                "flag": flag,
                "valid_flag": valid
            })
    return render(request, "problem_4.html", {
        "flag": "",
        "request": request,
        "valid_flag": "",
    })


def problem_5(request):
    assert request.session["username"]
    request.session["current_problem"] = 5
    items = list(Item.objects.raw(f"select * from problems_item"))
    if request.method == "POST":
        if check := check_flag(request):
            flag, valid = check
            return render(request, "problem_5.html", {
                "request": request,
                "flag": flag,
                "valid_flag": valid
            })
        elif "sql_injection_search" in request.POST and (form := Problem4SearchForm(request.POST)).is_valid():
            search_content = form.cleaned_data["search_content"]
            query = list(Item.objects.raw(f"select * from problems_item where description like '%%{search_content}%%'"))
            return render(request, "problem_5.html", {
                "username": request.session["username"],
                "request": request,
                "items": query
            })
    return render(request, "problem_5.html", {
        "flag": "",
        "request": request,
        "valid_flag": "",
        "items": items
    })
