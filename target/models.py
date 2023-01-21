from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.db.models import Count, Sum, Avg
from django.utils.safestring import mark_safe

# Create your models here.


class Target(models.Model):
    db_host = models.CharField(max_length=500, blank=True, null=True)
    db_port = models.CharField(max_length=500, blank=True, null=True)
    database = models.CharField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    priority = models.IntegerField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "target"


class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = [
            "db_host",
            "db_port",
            "database",
            "username",
            "password",
            "priority",
            "status",
        ]
