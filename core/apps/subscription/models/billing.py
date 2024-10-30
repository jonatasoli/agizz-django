from core.apps.base.models.custom_models import ModelMixin
from django.db import models
from dateutil.relativedelta import relativedelta
from django.utils import timezone


class Billing(ModelMixin):
    subscription = models.ForeignKey("subscription.UserSubscriptionPlan", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def generate_next_billing(self):
        next_due_date = self.get_next_due_date()
        return Billing.objects.create(
            subscription=self.subscription,
            amount=self.subscription.plan.price,
            due_date=next_due_date,
        )

    def get_next_due_date(self):
        interval = self.subscription.plan.interval
        if interval == "monthly":
            return self.due_date + relativedelta(months=1)
        elif interval == "weekly":
            return self.due_date + relativedelta(weeks=1)
        elif interval == "yearly":
            return self.due_date + relativedelta(years=1)
