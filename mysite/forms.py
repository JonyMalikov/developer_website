from django import forms

from .models import Message


class ContactForm(forms.ModelForm):
    """форма обратной связи"""

    class Meta:
        model = Message
        fields = ["name", "email", "subject", "massage"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "id": "name", "required": True}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "required": True,
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "subject",
                    "required": True,
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "message",
                    "required": True,
                    "rows": 10,
                }
            ),
        }
