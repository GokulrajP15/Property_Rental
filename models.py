from django.db import models
from accounts_app.models import CustomUser
from properties_app.models import Property

class RentalApplication(models.Model):
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rental_applications')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rental_applications')
    status = models.CharField(max_length=10, choices=(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ), default='pending')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.property.title} by {self.tenant.username}"

class RentalAgreement(models.Model):
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rental_agreements')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rental_agreements')
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    signed_by_tenant = models.BooleanField(default=False)
    signed_by_owner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agreement for {self.property.title} - {self.tenant.username}"

class Payment(models.Model):
    rental_agreement = models.ForeignKey(RentalAgreement, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment of {self.amount} for {self.rental_agreement}"