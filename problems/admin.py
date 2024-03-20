from django.contrib import admin
from problems.models import CTFUser, Item


class CTFUserAdmin(admin.ModelAdmin):
    list_display = ("email", "solved")


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "new", "description", "hair_type")


admin.site.register(CTFUser, CTFUserAdmin)
admin.site.register(Item, ItemAdmin)
