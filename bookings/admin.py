from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'service',
        'date',
        'time',
        'status',
        'created_at',
    )
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'service__name')
    list_editable = ('status',)
    ordering = ('-created_at',)
