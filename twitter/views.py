from django.shortcuts import render
from django.views import View


class SignUpView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        return render(request, "signup.html")
