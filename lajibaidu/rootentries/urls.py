from django.urls import path

from . import views

app_name = 'rootentries'



urlpatterns = [
    path('', views.index, name='index'),
    path('navigation',views.navigation, name='navigation')
]

