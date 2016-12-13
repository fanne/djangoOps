#coding:utf-8
from django.contrib import admin

# Register your models here.

from models import *


class OwGameServerAdmin(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport','addstatus')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']

class GnTestOwgameServerAdmin(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']

###====华丽分割线=======
class HwFormalOwGameAdmin(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport','addstatus')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']

class HwTestOwGameAdmin(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']

class HwAuditOwGameAdmin(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']

class GnTestOwgameAdmin(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']

class GnAuditOwGame(admin.ModelAdmin):
    list_display = ('serverid','servername','serverhost','serverport')
    search_fields = ['serverid','servername','serverhost','serverport']
    ordering = ['serverid']


admin.site.register(owgameserver,OwGameServerAdmin)
admin.site.register(gn_test_owgameserver,GnTestOwgameServerAdmin)

admin.site.register(hw_formal_owgame,HwFormalOwGameAdmin)
admin.site.register(hw_test_owgame,HwTestOwGameAdmin)
admin.site.register(hw_audit_owgame,HwAuditOwGameAdmin)

admin.site.register(gn_test_owgame,GnTestOwgameAdmin)
admin.site.register(gn_audit_owgame,GnAuditOwGame)