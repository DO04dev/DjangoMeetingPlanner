from django.shortcuts import render, get_object_or_404
from .models import Meeting
from .models import Room


# Create your views here.
def detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def room_list(request):
    #room = get_object_or_404(Room)
    return render(request, "meetings/room.html",
                  {"rooms": Room.objects.all()})

