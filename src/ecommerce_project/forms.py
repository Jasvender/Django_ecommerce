from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fname = forms.CharField(
                label='First Name',
                widget=forms.TextInput(
                    attrs = {
                        "class" : "form-control",
                        "placeholder" : "Enter Your First Name"
                        }
                    )
                )
    lname = forms.CharField(
                label='Last Name',
                widget=forms.TextInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Last Name"
                        }
                    )
                )
    email = forms.EmailField(
                widget=forms.EmailInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Email Address"
                        }
                    )
                )
    content = forms.CharField(
                widget=forms.Textarea(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Message"
                        }
                    )
                )

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if "gmail.com" not in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is wrong.")

class LoginForm(forms.Form):
    """docstring for LoginForm."""
    username = forms.CharField(
                label="User Name",
                widget=forms.TextInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Username"
                    }
                )
    )
    password = forms.CharField(
                label="Password",
                widget=forms.PasswordInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Password"
                    }
                )
    )
class RegisterForm(forms.Form):
    """docstring for LoginForm."""
    first_name = forms.CharField(
                label="First Name",
                widget=forms.TextInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your First Name"
                    }
                )
    )
    last_name = forms.CharField(
                label="Last Name",
                widget=forms.TextInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Last Name"
                    }
                )
    )
    email = forms.EmailField(
                label="Email Address",
                widget=forms.EmailInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Email Address"
                    }
                )
    )
    username = forms.CharField(
                label="User Name",
                widget=forms.TextInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Username"
                    }
                )
    )
    password = forms.CharField(
                label="Password",
                widget=forms.PasswordInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Password"
                    }
                )
    )
    password2 = forms.CharField(
                 label="Confirm Password",
                 widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username Is Taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(username=email)
        if qs.exists():
            raise forms.ValidationError("Email Is Taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password Must Match.")
        return data
