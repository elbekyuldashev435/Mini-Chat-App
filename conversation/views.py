from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages


from .models import PrivateMessage, Messages, Groups
from users.models import Users
from .forms import PrivateMessageForm, SendFileForm, SendGroupMessage
# Create your views here.


class ConversationView(View):
    def get(self, request, pk):
        my_profile = Users.objects.get(pk=request.user.pk)
        form = PrivateMessageForm()
        user_profile = Users.objects.get(pk=pk)
        all_messages = PrivateMessage.objects.filter(
            Q(sender=request.user, receiver__pk=pk) | Q(receiver=request.user, sender__pk=pk)
        ).order_by('timestamp')
        read = PrivateMessage.objects.filter(sender__pk=pk)
        for i in read:
            if not i.is_read:
                i.is_read = True
                i.save()
        context = {
            'my_profile': my_profile,
            'form': form,
            'user_profile': user_profile,
            'all_messages': all_messages,
        }
        return render(request, 'chat.html', context=context)

    def post(self, request, pk):
        form = PrivateMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = get_object_or_404(Users, pk=pk)
            message.save()
            messages.success(request, 'Message was sent')
        return redirect('conversation:chat', pk=pk)


class SendFileView(View):
    def get(self, request, pk):
        form = SendFileForm()
        return render(request, 'send_file.html', {'form': form})

    def post(self, request, pk):
        form = SendFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.sender = request.user
            file.receiver = get_object_or_404(Users, pk=pk)
            file.save()
            messages.success(request, 'File was sent')
            return redirect('conversation:chat', pk=pk)
        return render(request, 'send_file.html', {'form': form})


def choice_for_delete(request, pk):
    message = get_object_or_404(PrivateMessage, pk=pk, sender=request.user)
    return render(request, 'delete_message.html', {'pk': message.pk})


class DeleteMessageView(View):
    def get(self, request, pk):
        message = get_object_or_404(PrivateMessage, pk=pk)
        message.delete()
        messages.success(request, 'Message was deleted')
        return redirect('conversation:chat', pk=message.receiver.pk)


class DeleteChatView(View):
    def get(self, request, pk):
        all_messages = PrivateMessage.objects.filter(
            Q(sender=request.user, receiver__pk=pk) | Q(receiver=request.user, sender__pk=pk)
        )
        all_messages.delete()
        messages.success(request, 'Chat was deleted')
        return redirect('home:users-list')


class GroupMessageView(View):
    def get(self, request, pk):
        my_profile = Users.objects.get(pk=request.user.pk)
        group_picture = Groups.objects.get(pk=pk)
        all_messages = Messages.objects.filter(chat_room__id=pk)

        form = SendGroupMessage()
        for i in all_messages:
            print(i)
        context = {
            'form': form,
            'group_picture': group_picture,
            'my_profile': my_profile,
            'all_messages': all_messages,
        }
        return render(request, 'group_message.html', context=context)

    def post(self, request, pk):
        form = SendGroupMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.chat_room = get_object_or_404(Groups, pk=pk)
            message.save()
            messages.success(request, 'Message was sent')
        return redirect('conversation:group', pk=pk)