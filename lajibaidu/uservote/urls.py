from django.urls import path

from . import views

app_name = 'uservote'

urlpatterns = [
    path('', views.index, name='index'),
    path('adduser/', views.adduser, name='adduser'),
    path('ShowUserSht/',views.ShowUserSht,name='ShowUserSht'),
    path('showaddnewuser/',views.Showaddnewuser,name='showaddnewuser'),
    path('<int:user_ID>/delete/', views.delete, name='delete'),
]

