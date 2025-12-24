from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import Service
from .models import Booking
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required



@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        Booking.objects.create(
            user=request.user,
            service=service,
            date=request.POST['date'],
            time=request.POST['time'],
            address=request.POST['address'],
            phone=request.POST['phone']
        )
        return redirect('my_bookings')

    return render(request, 'bookings/book_service.html', {'service': service})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
        status='pending'
    )

    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, "Booking cancelled successfully.")

    return redirect('my_bookings')

@staff_member_required
def admin_bookings(request):
    status = request.GET.get('status')
    bookings = Booking.objects.all().order_by('-created_at')

    if status:
        bookings = bookings.filter(status=status)

    return render(request, 'bookings/admin_bookings.html', {
        'bookings': bookings
    })


@staff_member_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id)

    allowed_status = ['confirmed', 'completed', 'cancelled']

    if status in allowed_status:
        booking.status = status
        booking.save()

    return redirect('admin_bookings')
