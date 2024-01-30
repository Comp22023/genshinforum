from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Themes(models.Model):
    id = models.BigAutoField(primary_key=True)
    themename = models.TextField()
    themecontent = RichTextField()
    themeimg = models.ImageField(blank=True, null=True)

    class Meta():
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.themename