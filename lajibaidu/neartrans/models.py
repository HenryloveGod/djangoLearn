from django.db import models
# Create your models here.
from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone
from django.db import migrations

#wifi/bt 数据库设计

class definition_wifi_ver_table(models.Model):
    wifi_ver = models.CharField(max_length=200)
    def __str__(self):
        return self.wifi_ver
    class Meta:
        verbose_name_plural = "定义_wifi驱动版本列表"

class definition_bt_ver_table(models.Model):
    bt_ver = models.CharField(max_length=200)

    def __str__(self):
        return self.bt_ver
    class Meta:
        verbose_name_plural = "定义_蓝牙驱动版本列表"

class definition_env_table(models.Model):
    env = models.CharField(max_length=200) 

    def __str__(self):
        return self.env  
    class Meta:
        verbose_name_plural = "定义_测试场景列表"

class definition_bt_fail_table(models.Model):
    bt_fail = models.CharField(max_length=200)   

    def __str__(self):
        return self.bt_fail

    class Meta:
        verbose_name_plural = "定义_蓝牙fail列表"


class definition_wifi_fail_table(models.Model):
    wifi_fail = models.CharField(max_length=200)    
    def __str__(self):
        return self.wifi_fail
    class Meta:
        verbose_name_plural = "定义_wifi Fail列表"
class definition_phone_table(models.Model):
    phone_type  =   models.CharField(max_length=200)  
    wifi_chip_type  =   models.CharField(max_length=200) 
    sys_ver     =   models.CharField(max_length=200)  
    hwshare_ver =   models.CharField(max_length=200)  
    more_info   =   models.CharField(max_length=200)  

    def __str__(self):
        return self.phone_type

    class Meta:
        verbose_name_plural = "定义_Phone机型列表"

class definition_pc_table(models.Model):
    pc_type     = models.CharField(max_length=200) 
    sys_ver     = models.CharField(max_length=200)
    wifi_ver    = models.ForeignKey(definition_wifi_ver_table, on_delete=models.CASCADE)
    bt_ver      = models.ForeignKey(definition_bt_ver_table, on_delete=models.CASCADE)

    def __str__(self):
        return self.pc_type

    class Meta:
        verbose_name_plural = "定义_PC机型列表"


class test_id_belong_table(models.Model):
    record_time = models.DateTimeField(verbose_name='record_time',auto_now=True)         # 日期
   
    test_des = models.CharField(max_length=1000,unique = True)            #建议用日期+测试环境+pc+phone定义
    
    env = models.ForeignKey(definition_env_table, on_delete=models.CASCADE)
    pc = models.ForeignKey(definition_pc_table, on_delete=models.CASCADE)
    phone = models.ForeignKey(definition_phone_table, on_delete=models.CASCADE)
    more_info = models.CharField(max_length=1000)
    def __str__(self):
        return self.test_des

    class Meta:
        verbose_name_plural = "创建_测试任务ID列表" 

class test_bt_rfcomm_run_log_table(models.Model):

    test_id         = models.ForeignKey(test_id_belong_table, on_delete=models.CASCADE)
    test_No         = models.IntegerField()     
    socket_cnn      = models.IntegerField()                 #   -1 if fail
    socket_trans    = models.IntegerField()                 #   -1 if fail
    result          = models.CharField(max_length=10)       #   pass/fail
    bt_fail         = models.ForeignKey(definition_bt_fail_table, on_delete=models.CASCADE)
    remark_info     = models.CharField(max_length=512)      #   ip/port etc ...

    class Meta:
        verbose_name_plural = "日志_蓝牙rfcomm测试记录细表"

class test_softap_trans_run_log_table(models.Model):
    test_id         = models.ForeignKey(test_id_belong_table, on_delete=models.CASCADE)
    test_No         = models.IntegerField()
    bt_socket_cnn   = models.IntegerField()
    bt_socket_trans = models.IntegerField()
    create_softap   = models.IntegerField()
    connect_sofap   = models.IntegerField()
    tcp_udp_connect = models.IntegerField()
    tcp_udp_speed   = models.IntegerField()
    destroy_softap  = models.IntegerField()
    
    #result=models.CharFiled(max_length=4,choice=pass_fail)
    result          = models.CharField(max_length=4)        #   pass/fail
    bt_fail         = models.ForeignKey(definition_bt_fail_table, on_delete=models.CASCADE)
    wifi_fail       = models.ForeignKey(definition_wifi_fail_table, on_delete=models.CASCADE)
    remark_info     = models.CharField(max_length=512,null=True,blank=True)     #   ip/port etc ...


    class Meta:
        verbose_name_plural = "日志_softap传输细表" 


###########
#   分类


test_table_group={

    '蓝牙':[test_bt_rfcomm_run_log_table],
    'wifi':[test_softap_trans_run_log_table],

}

##########


####### 根据用户id， 测试成功率结果

class report_record_by_test_tool_table(models.Model):
    record_time = models.DateTimeField(default=timezone.now(),name = 'record_time')       # 日期
    test_id     = models.ForeignKey(test_id_belong_table, on_delete=models.CASCADE)
    run_count   = models.IntegerField()  
    run_time    = models.IntegerField()
    fail_count  = models.IntegerField()
    pass_yield  = models.FloatField() 

    class Meta:
        verbose_name_plural = "Report_测试工具上报结果列表" 


########################
#
#   以下为报表，定义刷新
#
########################

#   env     pc      phone   test_num    run_count   fail_count  pass_yield
#   rfcomm  mach_1  p30_1   2           5000        3           94%

class report_env_yield_table(models.Model):
    env     = models.ForeignKey(definition_env_table, on_delete=models.CASCADE)
    pc      = models.ForeignKey(definition_pc_table, on_delete=models.CASCADE)
    phone   = models.ForeignKey(definition_phone_table, on_delete=models.CASCADE)

    test_number             = models.IntegerField()         #测试*次数
    total_run_count         = models.IntegerField()         #总运行次数
    total_run_time          = models.IntegerField(default=0)
    total_run_fail_count    = models.IntegerField()         #总运行fail次数
    total_pass_yield        = models.FloatField()           #总运行良率

    class Meta:
        verbose_name_plural = "测试场景成功率报告"





