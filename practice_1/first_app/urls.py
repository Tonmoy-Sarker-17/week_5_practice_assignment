from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('pass_change2/',views.pass_change2,name='pass_change2'),
]