from django.db import models
from users.models import Users
# Create your models here.


class PrivateMessage(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='message_sender')
    message = models.TextField()
    file = models.FileField(upload_to='all/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='message_receiver')
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'private_message'

    def __str__(self):
        return f"sender: {self.sender.username} --> receiver: {self.receiver.username} --> is read: {'Yes' if self.is_read else 'No'}"

    def file_type(self):
        if self.file:
            if self.file.url.endswith('.mp4'):
                return 'video/mp4'
            elif self.file.url.endswith('.png'):
                return 'image/png'
            elif self.file.url.endswith('.jpg'):
                return 'image/jpg'
        return None


class Groups(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='owner', null=True)
    group_picture = models.ImageField(upload_to='all/group_picture/', blank=True, default='default/group_picture/group.png')
    name = models.CharField(max_length=150)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    members = models.ManyToManyField(Users, related_name='chatroom')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f"room: {self.name} --> {'private' if self.is_private else 'public'}"


class Messages(models.Model):
    chat_room = models.ForeignKey(Groups, on_delete=models.CASCADE)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f"room: {self.chat_room} --> sender: {self.sender}"