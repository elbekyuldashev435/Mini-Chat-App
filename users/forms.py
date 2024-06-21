from django import forms
from django.forms import CharField, ModelForm, PasswordInput
from .models import Users


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'status_message', 'password', 'profile_picture', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditProfileForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'status_message', 'password', 'profile_picture', 'first_name', 'last_name']