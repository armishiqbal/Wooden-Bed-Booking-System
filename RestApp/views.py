from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import generics
from .models import Bed, Booking
from .serializers import BookingSerializer, BedSerializer

# --- Web Frontend Views ---

def home_view(request):
    beds = Bed.objects.all().order_by('id')
    return render(request, 'home.html', {'beds': beds})


def add_booking_view(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        cell = request.POST.get('cell', '').strip()
        day = request.POST.get('day', '').strip()
        time = request.POST.get('time', '').strip()
        bed_detail = request.POST.get('bed_detail', '').strip()
        total_amount = request.POST.get('total_amount', '').strip()
        delivery_address = request.POST.get('delivery_address', '').strip()

        if customer_name and cell and delivery_address:
            booking = Booking.objects.create(
                customer_name=customer_name,
                cell=cell,
                day=day,
                time=time,
                bed_detail=bed_detail,
                total_amount=total_amount,
                delivery_address=delivery_address
            )
            return redirect('booking_success', pk=booking.pk)
        else:
            messages.error(request, "Please fill in all required fields.")

    initial_bed = request.GET.get('bed', '')
    initial_amount = request.GET.get('price', '')
    return render(request, 'add_booking.html', {
        'initial_bed': initial_bed,
        'initial_amount': initial_amount
    })


def booking_success_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_success.html', {'booking': booking})


# --- Django REST Framework (DRF) API Views ---

class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by('-id')
    serializer_class = BookingSerializer


class BookingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BedListAPIView(generics.ListAPIView):
    queryset = Bed.objects.all().order_by('id')
    serializer_class = BedSerializer
