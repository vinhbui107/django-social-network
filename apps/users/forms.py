from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Email"})
    )
    username = forms.CharField(
        label="",
        max_length=80,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "autofocus": True}
        ),
    )
    password1 = forms.CharField(
        label="",
        max_length=80,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
    password2 = forms.CharField(
        label="",
        max_length=80,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm your password"}
        ),
    )

    class Meta(UserCreationForm.Meta):
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
        model = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        max_length=80,
        widget=forms.TextInput(
            attrs={"placeholder": "Email", "autofocus": True}
        ),
    )
    password = forms.CharField(
        label="",
        max_length=80,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )

    class Meta:
        fields = (
            "username",
            "password",
        )
        model = get_user_model()
