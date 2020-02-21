from django.contrib import admin

# Register your models here.


from neartrans.models import definition_pc_table,definition_phone_table,definition_env_table
from neartrans.models import definition_bt_ver_table,definition_bt_fail_table
from neartrans.models import definition_wifi_fail_table,definition_wifi_ver_table
from neartrans.models import test_id_belong_table,test_bt_rfcomm_run_log_table,test_softap_trans_run_log_table

from neartrans.models import report_record_by_test_tool_table


class definition_pc_table_admin(admin.ModelAdmin):
    list_display = ('pc_type', 'sys_ver','wifi_ver','bt_ver') 
    fields = ('pc_type', 'sys_ver','wifi_ver','bt_ver')

class definition_phone_table_admin(admin.ModelAdmin):
    list_display = ('phone_type', 'sys_ver','hwshare_ver', 'wifi_chip_type','more_info') 
    fields = ('phone_type', 'sys_ver','hwshare_ver', 'wifi_chip_type','more_info')

class definition_env_table_admin(admin.ModelAdmin):
    list_display = ['env'] 
    fields = ['env']

class definition_bt_ver_table_admin(admin.ModelAdmin):
    list_display = ['bt_ver'] 
    fields =['bt_ver'] 
 
class definition_bt_fail_table_admin(admin.ModelAdmin):
    list_display = ['bt_fail'] 
    fields = ['bt_fail'] 

class definition_wifi_fail_table_admin(admin.ModelAdmin):
    list_display =['wifi_fail'] 
    fields = ['wifi_fail']


class definition_wifi_ver_table_admin(admin.ModelAdmin):
    list_display = ['wifi_ver'] 
    fields = ['wifi_ver']

class test_id_belong_table_admin(admin.ModelAdmin):
    list_display = ('record_time', 'test_des','env','pc','phone','more_info','chose_log_table') 
    fields = ('test_des','env','pc','phone','more_info','chose_log_table')


class test_bt_rfcomm_run_log_table_admin(admin.ModelAdmin):
    list_display = ('test_des','test_No','socket_cnn','socket_trans','result','bt_fail','remark_info') 
    fields = ('test_des','test_No','socket_cnn','socket_trans','result','bt_fail','remark_info')


class test_softap_trans_run_log_table_admin(admin.ModelAdmin):
    list_display = ('test_des','test_No','bt_socket_cnn','bt_socket_trans',
        'create_softap','connect_sofap','tcp_udp_connect','tcp_udp_speed','destroy_softap',
        'result','bt_fail','wifi_fail','remark_info') 
    fields = ('test_des','test_No','result','bt_fail','wifi_fail','remark_info','bt_socket_cnn','bt_socket_trans',
        'create_softap','connect_sofap','tcp_udp_connect','tcp_udp_speed','destroy_softap' ) 



class report_test_by_test_tool_table_admin(admin.ModelAdmin):
    list_display = ('test_des','run_count','run_time','fail_count','pass_yield')
    fields = ('test_des','run_count','run_time','fail_count','pass_yield')


admin.site.register(definition_pc_table,definition_pc_table_admin)
admin.site.register(definition_phone_table,definition_phone_table_admin)
admin.site.register(definition_env_table,definition_env_table_admin)
admin.site.register(definition_bt_ver_table,definition_bt_ver_table_admin)
admin.site.register(definition_bt_fail_table,definition_bt_fail_table_admin)
admin.site.register(definition_wifi_ver_table,definition_wifi_ver_table_admin)
admin.site.register(definition_wifi_fail_table,definition_wifi_fail_table_admin)

admin.site.register(test_id_belong_table,test_id_belong_table_admin)

admin.site.register(test_bt_rfcomm_run_log_table,test_bt_rfcomm_run_log_table_admin)
admin.site.register(test_softap_trans_run_log_table,test_softap_trans_run_log_table_admin)

admin.site.register(report_record_by_test_tool_table,report_test_by_test_tool_table_admin)




