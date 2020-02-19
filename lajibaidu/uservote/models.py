from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

from django.db import migrations



class UserSht(models.Model):

    record_time = models.DateTimeField('record_time')   # 日期
    user_id = models.CharField(max_length=200)    # 字符串
    user_name = models.CharField(max_length=200)    # 字符串
    user_info = models.CharField(max_length=200)    # 字符串
        
    def __str__(self):
        return self.user_name


class DailyReport(models.Model):
    user = models.ForeignKey(UserSht, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=200)     #
    is_ok = models.CharField(max_length=200)   
    detail_record_time = models.DateTimeField('detail_record_time')       # 日期
    
    def __str__(self):
        return self.is_ok




class poker_report_table(models.Model):
    user    = models.CharField(max_length=200)
    wang    = models.IntegerField(default=0)
    two     = models.IntegerField(default=0)
    one     = models.IntegerField(default=0)
    king     = models.IntegerField(default=0)
    queen      = models.IntegerField(default=0)
    jack    = models.IntegerField(default=0)
    ten     = models.IntegerField(default=0)
    nine    = models.IntegerField(default=0)
    eight   = models.IntegerField(default=0)
    seven   = models.IntegerField(default=0)
    six     = models.IntegerField(default=0)
    five    = models.IntegerField(default=0)
    four    = models.IntegerField(default=0)
    three   = models.IntegerField(default=0)

class poker_log_table(models.Model):
    user    = models.CharField(max_length=200)
    log     = models.CharField(max_length=200)
