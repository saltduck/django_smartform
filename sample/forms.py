from django import forms
from smartform import SmartForm


class SampleForm(SmartForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        form_id = 'id_form'
        form_name = 'form'
        form_class = ''
        form_action = ''
