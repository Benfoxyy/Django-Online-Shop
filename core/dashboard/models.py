from django.db import models
from accounts.validators import validate_iranian_cellphone_number


class TicketModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=12,
        validators=[validate_iranian_cellphone_number],
        null=True,
        blank=True,
    )
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def snippet(self):
        return self.description[:17] + "..."
