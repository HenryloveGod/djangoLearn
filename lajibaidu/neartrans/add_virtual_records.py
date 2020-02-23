

from neartrans.models import *






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