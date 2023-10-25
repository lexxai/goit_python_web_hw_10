from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )

    password1 = forms.CharField(
        label="Password",
        required=True,
        min_length=8,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )

    password2 = forms.CharField(
        label="Password confirmation",
        required=True,
        min_length=8,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )
    password = forms.CharField(
        max_length=25,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]


# class DeleteForm(forms.ModelForm):
#     username = forms.CharField(
#         max_length=100, required=True, widget=forms.HiddenInput()
#     )

#     class Meta:
#         model = User
#         fields = [
#             "username",
#         ]
