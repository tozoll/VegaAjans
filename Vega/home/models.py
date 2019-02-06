from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.
class HomePage(models.Model):
    created_by      = models.ForeignKey(User,on_delete=models.CASCADE)
    
    bgImage         = models.ImageField(verbose_name="Arkaplan Resmi",blank=True, null=True,upload_to="bg/")
    bgVideoMp4      = models.FileField(verbose_name="Arkaplan Video(.mp4)",blank=True, null=True,upload_to="bg/")
    bgVideoWebm     = models.FileField(verbose_name="Arkaplan Video(.webm)",blank=True, null=True,upload_to="bg/")
    bgVideoMobile   = models.ImageField(verbose_name="Arkaplan Video(mobile)",blank=True, null=True,upload_to="bg/")

    headerTop       = models.TextField(max_length=400,verbose_name="Üst Başlık")
    headerCenter    = models.TextField(max_length=400,verbose_name="Ana Başlık")
    headerBottom    = RichTextField()
    
    buttonText      = models.CharField(max_length=50,verbose_name="Buton Text")
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.headerTop
    
    class Meta:
        verbose_name            = "Ana Sayfa"
        verbose_name_plural     = "Ana Sayfa"
        ordering                = ["headerTop"]
