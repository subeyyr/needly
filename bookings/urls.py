from django.urls import path
from .views import book_service, my_bookings,cancel_booking,admin_bookings,update_booking_status

urlpatterns = [
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('dashboard/bookings/', admin_bookings, name='admin_bookings'),
    path(
        'dashboard/bookings/<int:booking_id>/<str:status>/',
        update_booking_status,
        name='update_booking_status'
    )

]
