from django.contrib import admin
from .models import Groups, Messages, PrivateMessage
# Register your models here.


admin.site.register(Groups)
admin.site.register(Messages)
admin.site.register(PrivateMessage)