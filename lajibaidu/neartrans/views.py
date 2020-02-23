from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.utils import timezone

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from neartrans.models import report_record_by_test_tool_table,test_id_belong_table

from neartrans.add_virtual_records import inser_defaults

from neartrans.models import BT_RFCOMM_LOG,WIFI_PIC_TRANS_LOG

from neartrans.models import test_bt_rfcomm_run_log_table,test_softap_trans_run_log_table

###########
#   分类
test_log_table_defines = {
    BT_RFCOMM_LOG:{
        'table':test_bt_rfcomm_run_log_table,
        'html':'neartrans/show_fail_detail_by_test_des_bt.html'
    },
    WIFI_PIC_TRANS_LOG:{
        'table':test_softap_trans_run_log_table,
        'html':'neartrans/show_fail_detail_by_test_des_wifi.html',
    },
}
##########





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
        test_id_table = test_report[0]
        logtable = test_log_table_defines[test_id_table.chose_log_table]['table']
        test_tool_report = logtable.objects.filter(test_des_id = fail_test_id,result='fail')

        dest_url =test_log_table_defines[test_id_table.chose_log_table]['html']
      
    except test_tool_report.DoesNotExist:
        raise  HttpResponse(content='未找到记录！')
 
    if test_tool_report.count() > 0:
        return render(request, dest_url,{"test_tool_report":test_tool_report,'test_id_table':test_id_table})
    else:
        
    
        return  HttpResponse(content='记录为0！')









