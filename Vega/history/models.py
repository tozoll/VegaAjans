import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

class HistoryHeader(models.Model):
    created_by   = models.ForeignKey(User,on_delete=models.CASCADE)
    header       = models.CharField(max_length=50, verbose_name="Başlık")
    content      = models.TextField(max_length=500,verbose_name="İçerik")
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name="Tarihçe Başlık"
        verbose_name_plural = "Tarihçe Başlık"


class HistoryYears(models.Model):
    created_by      = models.ForeignKey(User,on_delete=models.CASCADE)
    historyHeader   = models.ForeignKey(HistoryHeader,on_delete=models.CASCADE)
    icon            = models.FileField(verbose_name="Ikon",upload_to="history/")
    year            = models.PositiveIntegerField(verbose_name="Sene")
    content         = models.TextField(max_length=500,verbose_name="İçerik")
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.year)

    class Meta:
        verbose_name="Tarihçe İçerik"
        verbose_name_plural = "Tarihçe İçerik"
        ordering = ["pk","year"]

@receiver(post_delete, sender=HistoryYears)
def photo_post_delete_handler(sender, instance,**kwargs):
    if instance.icon:
        if os.path.isfile(instance.icon.path):
            os.remove(instance.icon.path)