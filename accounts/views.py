from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

class CustomLoginForm(AuthenticationForm):
    pass

class LoginView(View):
    def get(self, request):
        form = CustomLoginForm()
        return render(request, "../templates/registration/login.html", context={"form": form})

    def post(self, request):
        form = CustomLoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")

        return render(request, "../templates/registration/login.html", context={"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")
