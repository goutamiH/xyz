# importing HttResponse from library
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404, render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import *

# Create your views here. 
def registerUser(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, 'signup.html',{'form':form})
 
def LoginUser(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,'Login_page.html',{'form':form}) 
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return render(request,'home.html')
def nope(request):
	return render(request,"register.html")

def Contact(request):
    form=contact_Us_Form()
    if request.method=='POST':
        form=contact_Us_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data has been submitted')
            return redirect('home')
    context={'form':form}   
    return render(request,'contact_us_form.html',context)
 
def About(request):
	return render(request,'about_us.html')


@login_required(login_url='login')
def home(request):
    q=request.GET.get('q') if request.GET.get('q')!= None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics=Topic.objects.all()
    room_count=rooms.count()
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    participants=room.participants.all()
    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('comment')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    # for i in room:
    #     if i['id']==int(pk):
    #         room=i
    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form=Room_Form()
    topics=Topic.objects.all()
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')
    context={'form':form,'topics':topics}
    return render(request,'room_form.html',context)
def move(request):
    return HttpResponse("You have successfully created a  study Room")

@login_required(login_url='login')
def updateRoom(request,pk):
    room=get_object_or_404(Room, pk=pk)
    form=Room_Form(instance=room)
    topics=Topic.objects.all()
    if request.user != room.host:
       return HttpResponse("You're re not allowed here!>>>>>")
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        room.name=request.POST.get('name')
        room.topic=topic
        room.description=request.POST.get('description')
        room.save()
        return redirect('home')
          
    context={'form':form,'topics':topics,'room':room}
    return render(request,'room_form.html',context)
@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Please Login First, Can't delete this room")
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'delete.html', {'room': room})



@login_required(login_url='login')
def deleteMessage(request,pk):
    message=Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("Please Login First,Can't delete this room")
    if request.method=='POST':
        message.delete()
        return redirect('home')
    return render(request,'delete.html',{'obj':message})

def userprofile(request,pk):
    #user = get_object_or_404(User, pk=pk)
    user=User.objects.get(pk=pk)
    rooms=user.room_set.all()
    room_messages=user.message_set.all()
    topics=Topic.objects.all()
    context={'user':user, 'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'profile.html',context)

def Topics_collection(request):
    q=request.GET.get('q') if request.GET.get('q')!= None else ''
    topics=Topic.objects.filter(name__icontains=q)
    return render(request,'topics.html',{'topics':topics})

def Activity_Page(request):
    room_messages=Message.objects.all()
    return render(request,'activity_component.html',{'room_messages':room_messages})

@login_required(login_url='login')
def Update_user(request,pk):
    user = request.user
    form=Userform(instance=user)
    if request.method=='POST':
        form=Userform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile',user.id)
    return render(request,'Update_User.html',{'form':form})
