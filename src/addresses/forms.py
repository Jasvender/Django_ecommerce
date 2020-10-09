from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            # 'billing_profile',
            # 'address_type',
            'address_line_1','address_line_2','city','state','country','postal_code',
        ]
        widgets={
            'address_line_1':forms.Textarea(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your Address Line 1",
                    "rows" : "3"
                }
            ),
            'address_line_2':forms.Textarea(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your Address Line 2",
                    "rows" : "3"
                }
            ),
            'city':forms.TextInput(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your City"
                }
            ),
            'state':forms.TextInput(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your State"
                }
            ),
            'country':forms.TextInput(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your Country"
                }
            ),
            'postal_code':forms.TextInput(
                attrs={
                    "class" : "form-control mb-2",
                    "placeholder" : "Enter Your Postal Code"
                }
            )
        }
