from django.urls import path
from django.conf.urls import url
from . import views
from chat1 import settings
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('chat/', views.index, name="index"),
    path('',views.signup,name="signup"),
    url(r'^login/$', LoginView.as_view(template_name="userLogIn/login.html"), name='login'),
    url(r'^logout/$', LogoutView.as_view( next_page='/login/'), name='logout'),
    path("request/",views.friendrequest,name="request"),
    # path("acceptrequest/<int:requestID>/",views.accept_friendrequest, name="accept-friend-request"),
    path("show/",views.showNotifications,name="show"),
    path("user_profile/<int:my_id>", views.viewAccount,name="profile"),
    path("edit_profile/", views.edit_profile,name="edit_profile"),
    path("success/",views.success, name="success"),

    # path("update_profile/", views.update_profile,name=" update_profile"),
    # path("notification/",views.notification, name="notification"),
    # path('search/',views.SearchView.as_view()),
   
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)