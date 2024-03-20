from django import forms
from django.shortcuts import render, redirect

from problems.models import CTFUser


class RegisterForm(forms.Form):
    username = forms.CharField(label="username")


def home(request):
    if request.method == "POST":
        if (form := RegisterForm(request.POST)).is_valid():
            properties, exists = CTFUser.objects.get_or_create(
                email=form.cleaned_data["username"],
                defaults={
                    "email": form.cleaned_data["username"],
                    "solved": []
                }
            )
            request.session["current_problem"] = 1
            request.session["username"] = properties.email
            request.session["solved"] = properties.solved
            print(list(CTFUser.objects.all()))
            return redirect(f"/problems/1/")
    return render(request, "home.html")