from django.contrib import admin

from .models import complaints,completed
from .models import complaints,completed
class complaintsAdmin(admin.ModelAdmin):
    list_display=['name','service','phone','address','regdate','donedate','status']
    list_filter = ['regdate']
    change_list_template='admin/complaints/complaints_change_list1.html'
class completedAdmin(admin.ModelAdmin):
    list_display=['name','service','phone','address','regdate','donedate','status']
    list_filter=['regdate','donedate']

admin.site.register(complaints,complaintsAdmin)
admin.site.register(completed,completedAdmin)
admin.site.site_header='Kyb Communications Admin'