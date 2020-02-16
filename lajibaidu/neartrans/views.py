from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.utils import timezone
from .models import UserSht
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class IndexView(ListView):
 
    model = UserSht
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):

    users = UserSht.objects.all()

    for user in users:
        print(user)

    return render(request, 'root/index.html', {'users': users})

def adduser(request):

    id = request.POST['user_id']
    name = request.POST['user_name']
    info = request.POST['user_info']

    q = UserSht(user_id=id,user_name=name, record_time=timezone.now(),user_info=info)
    q.save()

    return index(request)











