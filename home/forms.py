from django import forms
from users.models import Users


class UserSearchForm(forms.Form):
    query = forms.CharField(max_length=150, label="Search", required=False)