from django.db import models


class LernModulesModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Name module")
    description = models.TextField(null=True, blank=True, verbose_name="Description module")
    number = models.CharField(max_length=32, verbose_name="Number module")

    class Meta:
        verbose_name = "Lern Module"
        verbose_name_plural = "Lern Modules"
