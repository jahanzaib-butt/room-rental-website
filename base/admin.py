from django.contrib import admin
from .models  import *
class productAdmin(admin.ModelAdmin):
    list_display = ('title','catagory','phone')  # Corrected spelling of 'category'
    list_filter = ('catagory',)
# Register your models here.
admin.site.register(Room,productAdmin)
admin.site.register(Message)
