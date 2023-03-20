from django.db import models
from django.utils import timezone

class TimestampModel(models.Model):
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(TimestampModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True