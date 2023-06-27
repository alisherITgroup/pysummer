from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Lesson, Problem, Attempt
from django.contrib.auth.decorators import login_required
import requests


def home(request):
    lesson = Lesson.objects.first()
    return render(request, "home.html", {
        "lesson": lesson
    })

def login_(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Ajoyib! PySummerga xush kelibsiz!")
            return HttpResponseRedirect(reverse_lazy("home"))
        else:
            messages.add_message(request, messages.ERROR, "Afsus! Foydalanuvchi nomi yoki kalit so'zi xato!")
            print("error")
            return HttpResponseRedirect(reverse_lazy("home"))
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Ajoyib! PySummerga xush kelibsiz!")
            return HttpResponseRedirect(reverse_lazy("home"))
        except Exception as e:
            print(e)
    return render(request, "home.html")

@login_required(login_url='login')
def lesson(request, url):
    lesson = Lesson.objects.all().filter(url=url).first()
    print(lesson)
    if lesson:
        problems = lesson.problems.all()
        is_next = False
        if request.user in lesson.enders.all():
            is_next = True
        return render(request, "lesson.html", {
            "lesson": lesson,
            "problems": problems,
            "is_next": is_next
        })
    else:
        return render(request, "404.html")
    
def solve(request, url, pk):
    token = "7f3b28a781ba850296fbd5ec5578f1787aa9e772"
    url = "https://algorithmshubtestapi.pythonanywhere.com/test/"
    if request.method == "POST":
        problem = Problem.objects.get(id=pk)
        code = request.POST.get("code")
        language = request.POST.get("language")
        tests = problem.tests
        data = {
            "name": request.user.username,
            "code": code,
            "language": language,
            "userinput": "",
            "tests": str(tests),
            "timelimit": 1000,
        }
        response = requests.post(
            url=url, 
            data=data,
            headers={
                "Authorization": f"Token {token}"
            }
        )
        response = response.json()
        print(response)