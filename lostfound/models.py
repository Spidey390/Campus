from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    STATUS_CHOICES = (('Lost', 'Lost'), ('Found', 'Found'))
    CATEGORY_CHOICES = (
        ('Electronics', 'Electronics'),
        ('ID Card', 'ID Card'),
        ('Books', 'Books'),
        ('Clothing', 'Clothing'),
        ('Other', 'Other'),
    )

    item_name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=200, help_text="Location where item was lost/found")
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False, help_text="Approved by admin (for found items)")

    def __str__(self):
        return f"{self.item_name} ({self.get_status_display()})"

class Claim(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    
    # All fields are now in one correct model
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='claims')
    claimant = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, help_text="Optional: For easier contact by the campus office.")
    claim_description = models.TextField(help_text="Provide a specific detail to prove ownership.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim for '{self.item.item_name}' by {self.claimant.username}"