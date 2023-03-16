from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.db.models import BaseModel
from django.conf import settings
import datetime


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)

    @property
    def is_subscription_active(self):
        return True

    @property
    def trial_period(self):
        if settings.TRIAL_PERIOD is not None:
            trial_period = settings.TRIAL_PERIOD
            if not isinstance(trial_period, int) or trial_period <= 0:
                raise TypeError("TRIAL_PERIOD must be +int only")
            today = datetime.date.today()
            days_passed = (today - self.created_at.date()).days
            return trial_period - days_passed
        return None
