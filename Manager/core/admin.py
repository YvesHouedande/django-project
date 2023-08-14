from django.contrib import admin

# Register your models here.
# your_project/admin.py

from django.contrib import admin
from .models import ProfileUtisateur, Product, Order, LigneOrder, Category
from .utils import update_stock_on_validation


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_commande', 'validation')
    list_filter = ('validation',)

    def save_model(self, request, obj, form, change):
        if obj.validation and not obj._state.adding:
            update_stock_on_validation(obj)
        super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)

admin.site.register(ProfileUtisateur)
admin.site.register(Product)
# admin.site.register(Order)
admin.site.register(LigneOrder)
admin.site.register(Category)

                    

