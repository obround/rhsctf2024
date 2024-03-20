from django.urls import path, include
from . import views

urlpatterns = [
    path("1/", views.problem_1, name="problem_1"),
    path("2/", views.problem_2, name="problem_2"),
    path("3/", views.problem_3, name="problem_3"),
    path("4/", views.problem_4, name="problem_4"),
    path("5/", views.problem_5, name="problem_5")
]
