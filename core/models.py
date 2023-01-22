from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.db.models import Count, Sum, Avg
from django.utils.safestring import mark_safe

# Create your models here.

from target.models import Target


class BackupHistory(models.Model):
    target = models.ForeignKey(
        "target.Target",
        on_delete=models.CASCADE,
        related_name="backup_history_location",
        null=False,
        blank=False,
    )
    path = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "backup_histories"
