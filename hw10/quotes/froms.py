from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Author

# fullname = models.CharField(max_length=120)
# born_date = models.CharField(max_length=50)
# born_location = models.CharField(max_length=120)
# description = models.TextField()
# created_at = models.DateTimeField(auto_now_add=True)


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter fullname"}
        ),
    )
    born_date = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    born_location = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]
