from django.contrib import admin
from django.utils.html import format_html
from cafe.models import User, menu_item, rating, order, bill

admin.site.site_header = "🍽️ Food Ordering System Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Dashboard"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'first_name', 'last_name', 'cafe_manager', 'phone_verified', 'order_count')
    list_filter = ('cafe_manager', 'phone_verified')
    search_fields = ('phone', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        ('Personal Information', {
            'fields': ('phone', 'first_name', 'last_name')
        }),
        ('Status', {
            'fields': ('phone_verified', 'cafe_manager', 'order_count')
        }),
        ('Important Dates', {
            'fields': ('date_joined', 'last_login'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('-date_joined',)


@admin.register(menu_item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'list_order')
    list_filter = ('category',)
    search_fields = ('name', 'category', 'desc')
    list_editable = ('list_order',)
    ordering = ('list_order',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'price', 'list_order')
        }),
        ('Details', {
            'fields': ('desc',)
        }),
        ('Image', {
            'fields': ('pic',)
        }),
    )


@admin.register(rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('name', 'r_date', 'comment_preview')
    list_filter = ('r_date',)
    search_fields = ('name', 'comment')
    readonly_fields = ('r_date',)
    ordering = ('-r_date',)
    fieldsets = (
        ('Review Information', {
            'fields': ('name', 'r_date')
        }),
        ('Review Content', {
            'fields': ('comment',)
        }),
    )

    def comment_preview(self, obj):
        if obj.comment:
            return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
        return '-'
    comment_preview.short_description = 'Comment'


@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'name', 'phone', 'table', 'price', 'order_time', 'bill_clear')
    list_filter = ('table', 'bill_clear')
    search_fields = ('name', 'phone', 'table')
    readonly_fields = ('order_id', 'order_time', 'items_preview')
    ordering = ('-order_time',)
    fieldsets = (
        ('Order Information', {
            'fields': ('order_id', 'name', 'phone')
        }),
        ('Items', {
            'fields': ('items_preview',)
        }),
        ('Details', {
            'fields': ('table', 'price', 'order_time')
        }),
        ('Status', {
            'fields': ('bill_clear',)
        }),
    )

    def items_preview(self, obj):
        if obj.items_json:
            return obj.items_json[:200]
        return '-'
    items_preview.short_description = 'Order Items'


@admin.register(bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'bill_total', 'bill_time')
    list_filter = ('bill_time',)
    search_fields = ('name', 'phone')
    readonly_fields = ('bill_time', 'items_preview')
    ordering = ('-bill_time',)
    fieldsets = (
        ('Bill Information', {
            'fields': ('name', 'phone')
        }),
        ('Items', {
            'fields': ('items_preview',)
        }),
        ('Amount', {
            'fields': ('bill_total',)
        }),
        ('Date & Time', {
            'fields': ('bill_time',)
        }),
    )

    def items_preview(self, obj):
        if obj.order_items:
            return obj.order_items[:200]
        return '-'
    items_preview.short_description = 'Bill Items'