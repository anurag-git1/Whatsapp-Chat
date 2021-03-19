from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate,logout
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib import auth, messages
# from django.views.generic import ListView
from django.http import JsonResponse
from .models import FriendRequest
from django.http import HttpResponse
from django.db.models import Q


def index(request,*args):
    # user = User.objects.all()
    # abc = request.user
    # print("user",abc.id)
    query = request.GET.get('search')
    print("da",query)

    data = []
    if query:
        postresult = User.objects.filter(username__startswith=query)
        print(postresult,"abdkjsfhsf")
        data = data + list(postresult)
        print("anurag nadda",data)
        for data in data:
            print("data",data.id)
    else:
        user = "No Result"

    # Notification...
    user = FriendRequest.objects.all()
    current_user = request.user.id
    print("current_user",current_user)
    no_of_notifications = FriendRequest.objects.filter(reciever = current_user).count()
    print("no_of_notifications", no_of_notifications)
   
    # Friend List...
    queryset = FriendRequest.objects.filter(status= 'a').values("reciever_id")
    print("queryset",queryset[0])
    # friend_list = FriendRequest.objects.filter(Q(status='a') & Q(sender_id = current_user) | Q(reciever_id = current_user ))
    friend_list = FriendRequest.objects.filter(Q(reciever_id = current_user) | Q(sender_id = current_user))
    print("friend_list",friend_list)
  
    context = {
        'current_user'          : current_user,
        'users'                 : user,
        'friend_list'           : friend_list,
        "result"                : data,
        "no_of_notifications"   : no_of_notifications,
    } 
    return render(request,"userLogIn/index.html", context)

def friendrequest(request):
    rid = request.GET.get('id')
    print("rid",rid)
    sid = request.GET.get('sid')
    print("sid",sid)

    # current_user = request.user
    # reciever = User.objects.get(id=userID)
    # print("reciever request",reciever)
    # frndrequest, created = FriendRequest.objects.get_or_create(sender_id= current_user, reciever_id= reciever)
    # print("friend request",frndrequest)
    # if created:
    #     return HttpResponse('friend request send')
    # else:
    #     return HttpResponse('friend request already send')

    data = FriendRequest(
    sender_id= sid,
    reciever_id= rid
    )
    user = FriendRequest.objects.values_list("reciever_id","sender_id")
    print("user",user)
    if FriendRequest.objects.filter((Q(reciever_id=rid) & Q(sender_id = sid)) | (Q(reciever_id=sid) & Q(sender_id = rid))).exists():
        print("request already send")
    else:
        data.save() 
    
    return render(request,"userLogIn/search.html",{ "data":data })



# def notification(request):
#     user = FriendRequest.objects.all()
#     abc = request.user
#     userslist = FriendRequest.objects.filter(reciever = abc).count()
#     print(userslist,"FriendRequest")
#     # if request.user.is_authenticated:
#     #     count = FriendRequest.objects.filter(is_seen=False).count()
#     #     print("count",count)
#     #     return {
#     #         'notifications_count': count
#     #     }
#     # else:
#     #     return dict()
#     return render(request,"userLogIn/index.html",{"userslist":userslist})


def showNotifications(request):
    user = FriendRequest.objects.all()
    current_user = request.user
    print("current_user",current_user)
    no_of_notifications = FriendRequest.objects.filter(reciever = current_user)
    if no_of_notifications:
        print(no_of_notifications)  
    accept_reject = ''
    if request.method == 'POST':
        accept_reject = FriendRequest.objects.get(id=request.POST.get("reciever_id"))
        print("accept_reject",accept_reject.id)
        accept_reject.status = request.POST.get("status")
        print("status",accept_reject.status)
        if accept_reject.status == "Accept":
            accept_reject.status = 'a'
            accept_reject.save()
            print("run")
        else:
            accept_reject.status = 'd'
            accept_reject.save()
            print("not run")
        
    return render(request,"userLogIn/show.html",{"user":user, "number":no_of_notifications,"accept_reject":accept_reject})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'userLogIn/signup.html', {'form': form})


