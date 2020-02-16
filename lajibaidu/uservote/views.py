from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.utils import timezone
from .models import UserSht
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from datetime import datetime



def bukeIndex():
    pass


class IndexView(ListView):
 
    model = UserSht
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):

    #用户列表
    allusers = UserSht.objects.all()
    paras = {
        'result':None,
        'allusers': allusers,
        }

    return render(request, 'root/index.html',paras)

def ShowUserSht(request):

    allusers = UserSht.objects.all()
    paras = {
        'result':None,
        'allusers': allusers,
        }

    return render(request, 'root/ShowUserSht.html',paras)


def Showaddnewuser(request):
    return render(request, 'root/newuser.html', None)

def Addrecord(request):
    return render(request, 'root/addrecord.html', None)

def adduser(request):
    q = UserSht(
        user_id=request.POST['user_id'],
        user_name=request.POST['user_name'], 
        user_info=request.POST['user_info'],
        record_time=timezone.now(),
        )
    q.save()

    return HttpResponseRedirect(reverse('uservote:index', args=None))

def delete(request,user_ID):
    try:
        theuser = UserSht.objects.get(id=user_ID)
        theuser.delete()
    except UserSht.DoesNotExist:
        return render(request, 'root/index.html',{"result":"user not exist "})

    return HttpResponseRedirect(reverse('uservote:index', args=None))


