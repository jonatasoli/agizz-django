from django.db import models

from core.apps.base.models.custom_models import ModelMixin, TimeStampedMixin


class SubscriptionPlan(ModelMixin):
    INTERVAL_CHOICES = (
        ("monthly", "Monthly"),
        ("weekly", "Weekly"),
        ("yearly", "Yearly"),
    )
    name = models.CharField(max_length=255)
    producer = models.ForeignKey("auth_local.User", on_delete=models.PROTECT)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    interval = models.CharField(max_length=20, choices=INTERVAL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subscribers = models.ManyToManyField(
        to="auth_local.User",
        through="UserSubscriptionPlan",
        related_name="subscriptions"
    )

    def __str__(self):
        return f"{self.name} ({self.get_interval_display()})"



class UserSubscriptionPlan(TimeStampedMixin):
    user = models.ForeignKey("auth_local.User", on_delete=models.PROTECT)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.name} - {self.plan.name}"
