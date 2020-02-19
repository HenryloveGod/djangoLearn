from django.urls import path

from . import views

app_name = 'neartrans'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),

    path('show_report_test_tool_record_html/',views.show_report_test_tool_record_html,name='show_report_test_tool_record_html'),
    path('get_fail_detail_by_test_id',views.get_fail_detail_by_test_id,name='get_fail_detail_by_test_id'),
]

