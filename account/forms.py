from allauth.account.forms import SignupForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class AuthorsSignupForm(SignupForm):

    def save(self, request):
        user = super(AuthorsSignupForm, self).save(request)
        authors_group = Group.objects.get(name='authors')
        authors_group.user_set.add(user)
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        ]

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['password'] = make_password(cleaned_data.get('password'))
        return cleaned_data

