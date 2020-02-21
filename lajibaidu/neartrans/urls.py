from django.urls import path

from . import views

app_name = 'neartrans'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),

    path('show_report_test_tool_record_html/',views.show_report_test_tool_record_html,name='show_report_test_tool_record_html'),
    path('<int:fail_test_id>/show_fail_detail_by_test_des/',views.show_fail_detail_by_test_des,name='show_fail_detail_by_test_des'),
    # add_default_records

    path('add_default_records/',views.add_default_records,name='add_default_records'),

]

