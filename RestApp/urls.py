from django.urls import path
from . import views

urlpatterns = [
    # Web HTML Views
    path('', views.home_view, name='home'),
    path('add/', views.add_booking_view, name='add_booking'),
    path('booking/success/<int:pk>/', views.booking_success_view, name='booking_success'),

    # REST API Endpoints (as defined in README)
    path('RestApp/bookings/', views.BookingListCreateAPIView.as_view(), name='api_bookings_list'),
    path('RestApp/bookings/<int:pk>/', views.BookingDetailAPIView.as_view(), name='api_booking_detail'),
    path('RestApp/beds/', views.BedListAPIView.as_view(), name='api_beds_list'),
]
