from django.contrib import admin
from .models import Shop, Product, Deal


class ShopAdmin(admin.ModelAdmin):
    list_display = ("shop_name", "contact", "location", "category", "contact_person", "email")
    list_display_links = ["shop_name"]
    list_editable = ("contact", "location", "contact_person")
    list_fields = ("shop_name", "contact", "location", "contact_person", "category", "email")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "discount", "old_price")
    list_display_links = ["product_name"]
    list_editable = ("price", "discount")
    search_fields = ("product_name", "price", "discount", "old_price")


class DealAdmin(admin.ModelAdmin):
    list_display = ("deal_name", "valid_from", "valid_till", "discount_percent")
    list_display_links = ["deal_name"]
    list_editable = ("valid_from", "valid_till")
    search_fields = ("valid_from", "valid_till", "discount_percent")


admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Deal, DealAdmin)

from shop.models import Event
from django.contrib.auth.models import Group

# admin.site.register(Event)
admin.site.unregister(Group)

admin.site.site_header = "Naya Heading"


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "venue", "manager", "description")
    list_editable = ("venue", "manager")
    search_fields = ("name", "date", "venue", "manager", "description")


admin.site.register(Event, EventAdmin)
