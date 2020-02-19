from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.utils import timezone

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from neartrans.models import report_record_by_test_tool_table


def index(request):

    return render(request, 'neartrans/index.html',None)




def show_report_test_tool_record_html(request):
    print('show_report_test_tool_record_html!!')
    test_tool_report = report_record_by_test_tool_table.objects.order_by('-record_time')[:10]
  
    return render(request, 'neartrans/show_report_test_tool_record.html',{"test_tool_report":test_tool_report})

def get_fail_detail_by_test_id(request):

    if request.method != "GET":
        return None

    test_id = request.GET['test_id']
    if test_id == None:
        return None
    
    return HttpResponse(content=test_id)











