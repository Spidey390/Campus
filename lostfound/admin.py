from django.contrib import admin
from .models import Item
from .models import Item, Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('item', 'claimant', 'phone_number', 'status', 'created_at')
    list_filter = ('status',)
    list_editable = ('status',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'status', 'category', 'reported_by', 'is_verified')
    list_filter = ('status', 'is_verified', 'category')
    search_fields = ('item_name', 'description')
    actions = ['mark_as_verified']

    def mark_as_verified(self, request, queryset):
        queryset.update(is_verified=True)
    mark_as_verified.short_description = "Mark selected items as verified"