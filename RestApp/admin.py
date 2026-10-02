from django.contrib import admin
from .models import Bed, Booking

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'size', 'created_at')
    list_filter = ('size',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'cell', 'bed_detail', 'total_amount', 'day', 'time', 'created_at')
    search_fields = ('customer_name', 'cell', 'bed_detail', 'delivery_address')
    list_filter = ('day',)
