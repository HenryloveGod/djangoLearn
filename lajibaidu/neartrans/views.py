from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.utils import timezone

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from neartrans.models import report_record_by_test_tool_table,test_id_belong_table

from neartrans.models import inser_defaults,test_log_table_defines



def add_default_records(request):
    inser_defaults()

    return  HttpResponse(content='已添加记录')

def index(request):

    return render(request, 'neartrans/index.html',None)




def show_report_test_tool_record_html(request):
    
    test_tool_report = report_record_by_test_tool_table.objects.order_by('id')[:10]
  
    return render(request, 'neartrans/show_report_test_tool_record.html',{"test_tool_report":test_tool_report})

def show_fail_detail_by_test_des(request,fail_test_id):

    try:
        test_report = test_id_belong_table.objects.filter(test_id = fail_test_id)
        logtable = test_log_table_defines[test_report[0].chose_log_table]
        test_tool_report = logtable.objects.filter(test_des_id = fail_test_id,result='fail')
    except test_tool_report.DoesNotExist:
        raise  HttpResponse(content='未找到记录！')
 
    if test_tool_report.count() > 0:
        return render(request, 'neartrans/show_fail_detail_by_test_des.html',{"test_tool_report":test_tool_report})
    else:
        return  HttpResponse(content='记录为0！')









