# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class Users(AbstractUser):
#     friends = models.ManyToManyField("User", blank=True)


# class Friend_Request(models.Model):
#     from_user = models.ForeignKey(Users, related_name='from_user', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(Users, related_name='to_user', on_delete=models.CASCADE)
