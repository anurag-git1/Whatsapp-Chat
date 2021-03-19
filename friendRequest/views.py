# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Friend_Request,Users

# # Create your views here.
# def send_friend_request(request,userID):
#     from_user = request.user
#     to_user = Users.objects.get(id=userID)
#     friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
#     print(friend_request)
#     if created:
#         return HttpResponse("friend request send")
#     else:
#         return HttpResponse("friend request was already send")


# def accept_friend_request(request,requestID):
#     friend_request = Friend_Request.objects.get(id=requestID)
#     print(friend_request)
#     if friend_request.to_user == request.user:
#         friend_request.to_user.friends.add(friend_request.from_user)
#         friend_request.from_user.friends.add(friend_request.to_user)
#         friend_request.delete()
#         return HttpResponse("friend request accepted")
#     else:
#         return HttpResponse("friend request not accepted")