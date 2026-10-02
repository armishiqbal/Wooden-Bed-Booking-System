from django.db import models

class Bed(models.Model):
    SIZE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Queen', 'Queen'),
        ('King', 'King'),
    ]

    name = models.CharField(max_length=150, help_text="e.g. Luxury Double Bed")
    price = models.IntegerField(help_text="Price in PKR")
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, default='Double')
    image_url = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bed"
        verbose_name_plural = "Beds"

    def __str__(self):
        return f"{self.name} (Bed ID: {self.id})"


class Booking(models.Model):
    customer_name = models.CharField(max_length=150)
    cell = models.CharField(max_length=30)
    day = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    bed_detail = models.CharField(max_length=200)
    total_amount = models.CharField(max_length=50)
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bed booking"
        verbose_name_plural = "Bed bookings"

    def __str__(self):
        return f"Booking #{self.id} - {self.customer_name} ({self.bed_detail})"
