from django.contrib import admin
from .forms import *
from  .models import *
# Register your models here.
admin.site.register(contact_us_model)
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message) 
admin.site.register(ShareStory) 
admin.site.register(Diary_Writing)