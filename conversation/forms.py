from django import forms
from .models import PrivateMessage, Messages, Groups


class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ('message',)


class SendFileForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ('file',)


class SendGroupMessage(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('message',)


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('name', 'members', 'group_picture', 'description')