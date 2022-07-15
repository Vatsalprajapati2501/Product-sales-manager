from django.contrib import admin

# Register your models here.
from .models import Pro,Signup,Product

class Proadmin(admin.ModelAdmin):
    list_display=['pname','price','des','review']
admin.site.register(Pro,Proadmin)
admin.site.register(Signup)
admin.site.register(Product)
