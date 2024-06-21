from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from users.models import Users
from conversation.models import PrivateMessage
# Create your views here.


class UserListView(View):
    def get(self, request):
        users = Users.objects.exclude(pk=request.user.id)
        my_profile = get_object_or_404(Users, pk=request.user.id)
        context = {
            'my_profile': my_profile,
            'users': users,
        }
        return render(request, 'home.html', context=context)