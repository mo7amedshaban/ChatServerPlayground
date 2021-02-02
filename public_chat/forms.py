from django import forms
from public_chat.models import PublicChat


class PublicChatForm(forms.ModelForm):
    class Meta:
        model = PublicChat

        fields = '__all__'
