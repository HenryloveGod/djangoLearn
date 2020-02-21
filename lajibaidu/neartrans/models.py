from django.db import models
# Create your models here.
from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone
from django.db import migrations


WIFI_PIC_TRANS_LOG = 'wifi_pic_trans_log'
BT_RFCOMM_LOG = 'bt_rfcomm_log'


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
    test_id = models.IntegerField(primary_key=True,verbose_name="ID")
    record_time = models.DateTimeField(verbose_name='record_time',auto_now=True)         # 日期
    test_des = models.CharField(max_length=1000,unique = True)            #建议用日期+测试环境+pc+phone定义
    env = models.ForeignKey(definition_env_table, on_delete=models.CASCADE)
    pc = models.ForeignKey(definition_pc_table, on_delete=models.CASCADE)
    phone = models.ForeignKey(definition_phone_table, on_delete=models.CASCADE)
    more_info = models.CharField(max_length=1000)

    log_table_choice=((WIFI_PIC_TRANS_LOG,WIFI_PIC_TRANS_LOG),(BT_RFCOMM_LOG,BT_RFCOMM_LOG))

    chose_log_table = models.CharField(
        verbose_name='选择对应的日志表',
        max_length=50,
        choices=log_table_choice,
        default=1,
    )

    def __str__(self):
        return '%s:%s'%(self.test_id,self.test_des)
    def get_test_des(self):
        return '%s:%s'%(self.test_id,self.test_des)

    class Meta:
        verbose_name_plural = "创建_测试任务ID列表" 

class test_bt_rfcomm_run_log_table(models.Model):

    test_des        = models.ForeignKey(test_id_belong_table, on_delete=models.CASCADE)
    test_No         = models.IntegerField()     
    socket_cnn      = models.IntegerField()                 #   -1 if fail
    socket_trans    = models.IntegerField()                 #   -1 if fail
    result          = models.CharField(max_length=10)       #   pass/fail
    bt_fail         = models.ForeignKey(definition_bt_fail_table, on_delete=models.CASCADE)
    remark_info     = models.CharField(max_length=512)      #   ip/port etc ...

    class Meta:
        verbose_name_plural = "日志_蓝牙rfcomm测试记录细表"

class test_softap_trans_run_log_table(models.Model):
    test_des         = models.ForeignKey(test_id_belong_table, on_delete=models.CASCADE)
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


test_log_table_defines={

    BT_RFCOMM_LOG:test_bt_rfcomm_run_log_table,
    WIFI_PIC_TRANS_LOG:test_softap_trans_run_log_table,

}

##########


####### 根据用户id， 测试成功率结果

class report_record_by_test_tool_table(models.Model):
    record_time = models.DateTimeField(default=timezone.now(),name = 'record_time')       # 日期
    test_des     = models.ForeignKey(test_id_belong_table, on_delete=models.CASCADE)
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





def inser_defaults():


    wifi_ver214 = definition_wifi_ver_table(wifi_ver = 'wifi_214')
    wifi_ver214.save()
    wifi_ver213 = definition_wifi_ver_table(wifi_ver = 'wifi_213')
    wifi_ver213.save()

    bt_ver214 = definition_bt_ver_table(bt_ver = 'bt_214')
    bt_ver214.save()
    bt_ver213 = definition_bt_ver_table(bt_ver = 'bt_213')
    bt_ver213.save()

    env_bt = definition_env_table(env = 'bt_rfcomm压测_pc_vs_phone')
    env_bt.save()
    env_wifi = definition_env_table(env = '一碰传图压力测试_phone_vs_pc_间隔35秒_销毁AP')
    env_wifi.save()

    bt_fail_null = definition_bt_fail_table(bt_fail = 'null')
    bt_fail_null.save()

    bt_fail1 = definition_bt_fail_table(bt_fail = 'bt_connect_fail')
    bt_fail1.save()
    bt_fail11 = definition_bt_fail_table(bt_fail = 'bt_socket_interupt_fail')
    bt_fail11.save()
    bt_fail12 = definition_bt_fail_table(bt_fail = 'bt_driver_crash')
    bt_fail12.save()


    wifi_fail_null = definition_wifi_fail_table(wifi_fail = 'null')
    wifi_fail_null.save()
    wifi_fail1 = definition_wifi_fail_table(wifi_fail = 'tcp_socket_interupt_fail')
    wifi_fail1.save()
    wifi_fail2 = definition_wifi_fail_table(wifi_fail = 'create_softap_fail')
    wifi_fail2.save()
    wifi_fail3 = definition_wifi_fail_table(wifi_fail = 'destroy_softap_fail')
    wifi_fail3.save()
    wifi_fail4 = definition_wifi_fail_table(wifi_fail = 'softap_scan_fail')
    wifi_fail4.save()
    wifi_fail5 = definition_wifi_fail_table(wifi_fail = 'softap_arp_fail')
    wifi_fail5.save()
    wifi_fail6 = definition_wifi_fail_table(wifi_fail = 'softap_dhcp_fail')
    wifi_fail6.save()

    pc_mach = definition_pc_table(pc_type = 'mach',sys_ver = '18836.1117',wifi_ver=wifi_ver214,
        bt_ver = bt_ver214,
    )
    pc_mach.save()

    pc_kelvin = definition_pc_table(pc_type = 'kelvin',sys_ver = '18836.1117',wifi_ver=wifi_ver213,
        bt_ver = bt_ver213,
    )
    pc_kelvin.save()

    phone_30 = definition_phone_table(phone_type = 'p30',sys_ver = 'android10.0.0',wifi_chip_type='hisi301',
        hwshare_ver = 'hw_10.0.0', more_info = 'morexxxxx'
    )
    phone_30.save()

    phone_mate20 = definition_phone_table(phone_type = 'mate20',sys_ver = 'android10.0.0',wifi_chip_type='hisi301',
        hwshare_ver = 'hw_10.0.0', more_info = 'morexxxxx'
    )
    phone_mate20.save()


    test_id1 = test_id_belong_table(test_id = 1,record_time = timezone.now(),test_des='0220_蓝牙rfcomm压测',
        env = env_bt, pc=pc_kelvin, phone = phone_mate20,
        more_info = '0220',
        chose_log_table = WIFI_PIC_TRANS_LOG,
    )
    test_id1.save()

    test_id2 = test_id_belong_table(test_id = 2,record_time = timezone.now(),test_des='0221_wifi热点压测—销毁ap',
        env = env_wifi, pc=pc_mach, phone = phone_30,
        more_info = '0220',
        chose_log_table = BT_RFCOMM_LOG,
    )
    test_id2.save()

    test_log_bt_1 = test_bt_rfcomm_run_log_table(test_des = test_id1,test_No = 1,socket_cnn = 2,
        socket_trans =3, result = 'pass',bt_fail = bt_fail_null,remark_info = 'null',
    )
    test_log_bt_1.save()

    test_log_bt_2 = test_bt_rfcomm_run_log_table(test_des = test_id1,test_No = 2,socket_cnn = 2,
        socket_trans =121, result = 'pass',bt_fail = bt_fail_null,remark_info = 'null',
    )
    test_log_bt_2.save()

    test_log_bt_3 = test_bt_rfcomm_run_log_table(test_des = test_id1,test_No = 3,socket_cnn = 2,
        socket_trans =3, result = 'pass',bt_fail = bt_fail1,remark_info = 'null',
    )
    test_log_bt_3.save()

    test_log_bt_4 = test_bt_rfcomm_run_log_table(test_des = test_id1,test_No = 4,socket_cnn = 2,
        socket_trans =121, result = 'pass',bt_fail = bt_fail12,remark_info = 'null',
    )
    test_log_bt_4.save()

    test_log_bt_5 = test_bt_rfcomm_run_log_table(test_des = test_id1,test_No = 5,socket_cnn = 2,
        socket_trans =121, result = 'pass',bt_fail = bt_fail12,remark_info = 'null',
    )
    test_log_bt_5.save()




    test_log_wifi_1 = test_softap_trans_run_log_table(
        test_des = test_id2,test_No = 1,
        bt_socket_cnn = 2,
        bt_socket_trans =121, 
        create_softap = 1, connect_sofap = 2,tcp_udp_connect =3 , 
        tcp_udp_speed = 0 ,destroy_softap = 3,
        
        result = 'pass',bt_fail = bt_fail_null,wifi_fail = wifi_fail_null,remark_info = 'null',
    )
    test_log_wifi_1.save()

    test_log_wifi_2 = test_softap_trans_run_log_table(
        test_des = test_id2,test_No = 2,
        bt_socket_cnn = 2,
        bt_socket_trans =121, 
        create_softap = 1, connect_sofap = 2,tcp_udp_connect =3 , 
        tcp_udp_speed = 0 ,destroy_softap = 3,
        
        result = 'pass',bt_fail = bt_fail_null,wifi_fail = wifi_fail_null,remark_info = 'null',
    )
    test_log_wifi_2.save()

    test_log_wifi_3 = test_softap_trans_run_log_table(
        test_des = test_id2,test_No = 2,
        bt_socket_cnn = 2,
        bt_socket_trans =121, 
        create_softap = 1, connect_sofap = 2,tcp_udp_connect =3 , 
        tcp_udp_speed = 0 ,destroy_softap = 3,
        
        result = 'pass',bt_fail = bt_fail_null,wifi_fail = wifi_fail_null,remark_info = 'null',
    )
    test_log_wifi_3.save()

    test_log_wifi_4 = test_softap_trans_run_log_table(
        test_des = test_id2 , test_No = 2,
        bt_socket_cnn = 2,
        bt_socket_trans = 121, 
        create_softap = 1, connect_sofap = 2,tcp_udp_connect =3 , 
        tcp_udp_speed = 0 ,destroy_softap = 3,
        
        result = 'pass',bt_fail = bt_fail_null,wifi_fail = wifi_fail_null,remark_info = 'null',
    )
    test_log_wifi_4.save()

    test_log_wifi_4 = test_softap_trans_run_log_table(
        test_des = test_id2 , test_No = 2,
        bt_socket_cnn = 2,
        bt_socket_trans = 121, 
        create_softap = 1, connect_sofap = 2,tcp_udp_connect =3 , 
        tcp_udp_speed = 0 ,destroy_softap = 3,
        
        result = 'fail',bt_fail = bt_fail_null,wifi_fail = wifi_fail1,remark_info = 'null',
    )
    test_log_wifi_4.save()


    test_log_wifi_4 = test_softap_trans_run_log_table(
        test_des = test_id2 , test_No = 2,
        bt_socket_cnn = 2,
        bt_socket_trans = 121, 
        create_softap = 1, connect_sofap = 2,tcp_udp_connect =3 , 
        tcp_udp_speed = 0 ,destroy_softap = 3,
        
        result = 'fail',bt_fail = bt_fail_null,wifi_fail = wifi_fail1,remark_info = 'null',
    )
    test_log_wifi_4.save()


    report_test_record_bt = report_record_by_test_tool_table(record_time = timezone.now(),
        test_des = test_id1,run_count = 5,
        run_time =121, fail_count = 3,pass_yield = 0.40,
    )

    report_test_record_bt.save()

    report_test_record_bt = report_record_by_test_tool_table(record_time = timezone.now(),
        test_des = test_id2,run_count = 5,
        run_time =121, fail_count = 2,pass_yield = 0.60,
    )

    report_test_record_bt.save()