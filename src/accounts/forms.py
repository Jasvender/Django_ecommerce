from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name','email',)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name','email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class GuestForm(forms.Form):
    email = forms.EmailField(
                label="Email Address",
                widget=forms.EmailInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Email Address"
                    }
                )
    )

class LoginForm(forms.Form):
    """docstring for LoginForm."""
    email = forms.EmailField(
                label="Email",
                widget=forms.TextInput(
                    attrs={
                        "class" : "form-control",
                        "placeholder" : "Enter Your Email For Login"
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
class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(
                    label='Password',
                    widget=forms.PasswordInput(
                        attrs={
                            "class" : "form-control mb-2",
                            "placeholder" : "Enter Your Password"
                        }
                    )
                )
    password2 = forms.CharField(
                    label='Password confirmation',
                    widget=forms.PasswordInput(
                        attrs={
                            "class" : "form-control",
                            "placeholder" : "Enter Your Confirm Password"
                        }
                    )
                )

    class Meta:
        model = User
        fields = ('full_name','email',)
        widgets={
            'full_name':forms.TextInput(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your Full Name"
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your Email"
                }
            )
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False
        if commit:
            user.save()
        return user
# class RegisterForm(forms.Form):
#     """docstring for LoginForm."""
#     first_name = forms.CharField(
#                 label="First Name",
#                 widget=forms.TextInput(
#                     attrs={
#                         "class" : "form-control",
#                         "placeholder" : "Enter Your First Name"
#                     }
#                 )
#     )
#     last_name = forms.CharField(
#                 label="Last Name",
#                 widget=forms.TextInput(
#                     attrs={
#                         "class" : "form-control",
#                         "placeholder" : "Enter Your Last Name"
#                     }
#                 )
#     )
#     email = forms.EmailField(
#                 label="Email Address",
#                 widget=forms.EmailInput(
#                     attrs={
#                         "class" : "form-control",
#                         "placeholder" : "Enter Your Email Address"
#                     }
#                 )
#     )
#     username = forms.CharField(
#                 label="User Name",
#                 widget=forms.TextInput(
#                     attrs={
#                         "class" : "form-control",
#                         "placeholder" : "Enter Your Username"
#                     }
#                 )
#     )
#     password = forms.CharField(
#                 label="Password",
#                 widget=forms.PasswordInput(
#                     attrs={
#                         "class" : "form-control",
#                         "placeholder" : "Enter Your Password"
#                     }
#                 )
#     )
#     password2 = forms.CharField(
#                  label="Confirm Password",
#                  widget=forms.PasswordInput(
#                     attrs={
#                         "class" : "form-control",
#                         "placeholder" : "Enter Your Confirm Password"
#                     }
#                 )
#     )
#
#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("Username Is Taken")
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         qs = User.objects.filter(username=email)
#         if qs.exists():
#             raise forms.ValidationError("Email Is Taken")
#         return email
#
#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password2 != password:
#             raise forms.ValidationError("Password Must Match.")
#         return data
