from django.contrib import admin

from django.contrib import admin
from uservote.models import *

# Register your models here.


class UserShtConfig(admin.ModelAdmin):
    """自定制类  使得在admin数据库管理页面可以看到自己想要看的信息"""
    list_display = ["record_time", "user_id","user_name","user_info"]  # 多对多字段不可以用于此处
    list_display_links = ["user_name"]  # 设置可链接的字段  设置后，点击该字段便可以进入编辑页面
    list_filter = ["user_name"]  # 以所设置的字段作为筛选器 进行记录查询
    list_editable = ["user_info"]  # 设置可编辑字段，注意：如果在list_display_links中设置了的字段，在此处不可以再设置
    search_fields = [ "user_info","user_name"]  # 设置检索字段（模糊查询：输入关键字即可查询）
    date_hierarchy = "record_time"  # 过滤日期

    # action：批量操作记录
    def func(self, request, queryset):  # request：请求  queryset：所选中的那些你想要操作的数据
        print(self, request, queryset)
        # 对选中记录作操作：
        
    func.short_description = "显示用户信息"
    actions = [func,]

    fields = ["user_id", "user_name", "user_info"]  # 在添加记录的页面显示的字段
    # exclude = ["pub_date"]  # 在添加记录的页面不显示的字段，与fields相反

    ordering = ["id"]  # 按id升序排列   降序用["-id"]


class DailyReportConfig(admin.ModelAdmin):
    """自定制类  使得在admin数据库管理页面可以看到自己想要看的信息"""
    list_display = ["current_location","detail_record_time",'is_ok']  # 多对多字段不可以用于此处
    list_display_links = ["current_location"]  # 设置可链接的字段  设置后，点击该字段便可以进入编辑页面
    list_filter = ["is_ok"]  # 以所设置的字段作为筛选器 进行记录查询
    list_editable = ["is_ok"]  # 设置可编辑字段，注意：如果在list_display_links中设置了的字段，在此处不可以再设置
    search_fields = ["is_ok"]  # 设置检索字段（模糊查询：输入关键字即可查询）
    date_hierarchy = "detail_record_time"  # 过滤日期

    # action：批量操作记录
    def func(self, request, queryset):  # request：请求  queryset：所选中的那些你想要操作的数据
        print(self, request, queryset)
        # 对选中记录作操作：
        #queryset.update(pub_date="2012-1-1")  # 将所选记录的出版日改为2012年1月1日
    func.short_description = "无"
    #actions = [func,]

    fields = ["detail_record_time", "current_location", "is_ok"]  # 在添加记录的页面显示的字段
    # exclude = ["pub_date"]  # 在添加记录的页面不显示的字段，与fields相反

    ordering = ["id"]  # 按id升序排列   降序用["-id"]



admin.site.register(UserSht, UserShtConfig)  

print(admin.site._registry)

admin.site.register(DailyReport,DailyReportConfig)
