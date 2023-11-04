from django.contrib import admin
from .models import StockMarketTaskData
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class MyAppAdmin(admin.ModelAdmin):
    list_per_page = 1000
    class Meta:
        model = StockMarketTaskData
        
class StockMarketTaskResource(resources.ModelResource):
    class Meta:
        model = StockMarketTaskData

class StockMarketTaskAdmin(ImportExportModelAdmin):
    resource_class = StockMarketTaskResource

admin.site.register(StockMarketTaskData, StockMarketTaskAdmin)