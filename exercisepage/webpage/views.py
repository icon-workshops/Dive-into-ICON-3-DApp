from django.shortcuts import render
import os

DIR_PATH = os.path.abspath(os.path.dirname('__file__'))


def welcome(request):
    return render(request, "welcome.html")


def scrooge(request):
    return render(request, "scrooge.html")


def sample(request):
    return render(request, "iconex_connect_sample.html")


# exercise_welcome, exercise_scrooge 는 각각의 연습 코드로 라우팅해 주는 메서드이다.
def exercise_welcome(request):
    return render(request, "exercise/welcome.html")


def exercise_scrooge(request):
    return render(request, "exercise/scrooge.html")
