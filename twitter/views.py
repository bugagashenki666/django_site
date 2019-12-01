from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect, render, reverse
from .models import Message


class IndexView(View):
    def get(self, request):
        messages = Message.objects.all()
        return render(request, "index.html", {"messages": messages})

    def post(self, request):
        text = request.POST["text"]
        message = Message(text=text, author=request.user)
        message.save()
        return self.get(request)


class SignUpView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect(reverse("index"))


class SignInView(View):
    def get(self, request):
        return render(request, "signin.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("index"))
        return render(request, "signin.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("signin"))
