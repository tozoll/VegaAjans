from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class About(models.Model):
    created_by      = models.ForeignKey(User,on_delete=models.CASCADE)

    header          = models.CharField(max_length=50,verbose_name="Başlık")
    content         = RichTextField()

    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name            = "Biz"
        verbose_name_plural     = "Biz"
        ordering                = ["header"]
