from knox import views as knox_views
from .views import LoginAPI,RegisterAPI,Createcontactview,getallUsers,getuserdetails,getsingleUsers,CustomUserView,message,getmessages
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('addcontact/',Createcontactview.as_view(),name='createcontact'),
    path('getuserdetails/',getuserdetails,name='getuserdetails'),
    path('getallusers/',getallUsers,name="getallUsers"),
    path('getsingleusers/<int:id>',getsingleUsers,name="getsingleUsers"),
    path('profileupdate',CustomUserView.as_view(),name='custouserdetails'),
    path('message/',message,name="message"),
    path('getmessages/<int:sid>/<int:rid>',getmessages,name="getmessages")
]