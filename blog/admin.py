from django.contrib import admin
from .models import Sale,Add,Lap,Laptop
# Register your models here.
admin.site.register(Sale)
admin.site.register(Add)
admin.site.register(Lap)
@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}
































