from django import forms


class Contact(forms.Form):
    text=forms.CharField(max_length=500,label='your message')