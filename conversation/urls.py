from django.urls import path
from .views import ConversationView, choice_for_delete, DeleteMessageView, SendFileView, DeleteChatView, GroupMessageView
from .views import CreateGroupView

app_name = 'conversation'
urlpatterns = [
    path('chat/<int:pk>/', ConversationView.as_view(), name='chat'),
    path('send-file/<int:pk>/', SendFileView.as_view(), name='send-file'),
    path('delete-chat/<int:pk>/', DeleteChatView.as_view(), name='delete-chat'),
    path('choice-for-delete/<int:pk>/', choice_for_delete, name='choice-for-delete'),
    path('delete-message/<int:pk>/', DeleteMessageView.as_view(), name='delete-message'),

    path('group/<int:pk>/', GroupMessageView.as_view(), name='group'),
    path('create-group/', CreateGroupView.as_view(), name='create-group'),
]