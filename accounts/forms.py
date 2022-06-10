from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '영어 소문자 대문자, 숫자만 가능'
    }))
    nickname = forms.CharField(label='별명')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)  # ('username', 'email',)

    def save(self):
        user = super().save()
        new_profile = Profile.objects.create(
            user = user,
            nickname=self.cleaned_data.get('nickname')  # self.cleaned_date['nickname']
        )
        return new_profile