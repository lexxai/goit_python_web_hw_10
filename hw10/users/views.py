from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import RegisterForm, LoginForm, DeleteForm




class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"


    def get(self, request):
        if request.user.is_authenticated:
            return redirect(to="quotes:main")
        return render(request, self.template_name, context={ "form": self.form_class })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data["username"]
            messages.success(request, f"Your account '{username}' was created...")
            return redirect(to="users:login")
        else:
            messages.error(request, "Not registered...")
            return render(request, self.template_name, context={"form": form})

        

def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotes:main")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data["username"]
            messages.success(request, f"Your account '{username}' was created...")
            return redirect(to="users:login")
        else:
            messages.error(request, "Not registered...")
            return render(request, "users/signup.html", context={"form": form})

    return render(request, "users/signup.html", context={"form": RegisterForm()})




def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotes:main")

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="users:login")

        login(request, user)
        return redirect(to="quotes:main")

    return render(request, "users/login.html", context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:main')


@login_required
def deleteuser(request):
    if not request.user.is_authenticated:
        return redirect(to="quotes:main")

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.data.get("username") == request.user.username:       
            if request.user.delete():
                messages.success(request, 'User was deleted successfully')
                return redirect(to="quotes:main")
            else:
                messages.error(request, 'User was not deleted')
        else:
            messages.error(request, f'User was not deleted. Data of form is wrong {form.data["username"]=}, {request.user.username=}')

    return render(request, "users/delete.html", context={"form": DeleteForm(), "username":request.user })

