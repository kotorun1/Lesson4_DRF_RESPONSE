from django.contrib import admin
from .models import Workers, JobTitles, Orders
# Register your models here.

admin.site.register(Workers)
admin.site.register(JobTitles)
admin.site.register(Orders)
