from django.contrib import admin

#import our class
from .models import Meeting
from .models import Room

#register it so it can show in the user interface
admin.site.register(Meeting)
admin.site.register(Room)
