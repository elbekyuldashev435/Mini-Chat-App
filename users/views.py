from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .models import Users
from conversation.models import Groups
# Create your views here.


def get_choice(request):
    return render(request, 'choice_enter.html')


class MyProfileView(View):
    def get(self, request):
        user = Users.objects.get(pk=request.user.pk)
        groups = Groups.objects.filter(Q(owner=user))
        print(groups)
        context = {
            'user': user,
            'groups': groups
        }
        return render(request, 'my_profile.html', context)


class ProfileView(View):
    def get(self, request, pk):
        user = Users.objects.get(pk=pk)
        groups = Groups.objects.filter(Q(owner=user))
        context = {
            'user': user,
            'groups': groups
        }
        return render(request, 'profile.html', context)


class Registration(View):
    def get(self, request):
        registration_form = RegistrationForm()
        context = {
            'registration_form': registration_form
        }
        return render(request, 'registration.html', context=context)

    def post(self, request):
        registration_form = RegistrationForm(data=request.POST, files=request.FILES)
        if registration_form.is_valid():
            print(f"{request.user} is valid")
            registration_form.save()
            return redirect('users:login')
        else:
            context = {
                'registration_form': registration_form
            }
            print(f'user -{request}  invalid')
            return render(request, 'registration.html', context=context)


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            account = login_form.get_user()
            login(request, account)
            return redirect('home:users-list')

        else:
            context = {
                'login_form': login_form
            }
            return render(request, 'login.html', context=context)


class Logout(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('users:users')


class EditProfile(View):
    def get(self, request, pk):
        profile = Users.objects.get(pk=pk)
        edit_profile_form = EditProfileForm(instance=profile)
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'edit_profile.html', context=context)

    def post(self, request, pk):
        profile = Users.objects.get(pk=pk)
        edit_profile_form = EditProfileForm(request.POST, instance=profile)
        if edit_profile_form.is_valid():
            user = edit_profile_form.save(commit=False)
            password = edit_profile_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('profile')
        else:
            context = {
                'edit_profile_form': edit_profile_form
            }
            return render(request, 'edit_profile.html', context=context)