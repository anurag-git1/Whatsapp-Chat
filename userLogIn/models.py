
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    friends = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.user.username

class FriendRequest(models.Model):
    sender   = models.ForeignKey(User, on_delete=models.CASCADE,related_name="sender")
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever")
    Friend_request_status = (
        ('a', 'Accepted'),
        ('d', 'Decline'),
        ('c', 'Cancel'),
        ('r', 'Remove'),
        ('p', 'Pending'),
    )

    status = models.CharField(blank=True, default='p', choices=Friend_request_status, max_length=1)

    def __str__(self):
        return self.sender.username

