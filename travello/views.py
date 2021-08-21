from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    # dest1 = Destination()
    # dest1.name = 'Dhaka'
    # dest1.desc='The City never Sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price= 900
    # dest1.offer= False

    # dest2 = Destination()
    # dest2.name = 'Chitagong'
    # dest2.desc='The City of Food'
    # dest2.img='destination_2.jpg'
    # dest2.price= 300
    # dest2.offer=True

    # dest3 = Destination()
    # dest3.name = 'Coxs Bazar'
    # dest3.desc='The City of Sea'
    # dest3.img = 'destination_3.jpg'
    # dest3.price= 1300
    # dest3.offer= False

    # dests = [dest1,dest2,dest3]

    return render(request,"index.html",{'dests':dests})
