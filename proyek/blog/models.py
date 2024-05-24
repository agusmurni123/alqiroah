from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class User(AbstractUser):
    admin = models.BooleanField('Admin',default=False)
    staff = models.BooleanField('Staff',default=False)

class IndexWeb(models.Model):
    judul = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to='redaksi')
    paragraf = models.TextField()
    penulis = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    tanggal = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=60, blank=True)

    class Meta:
        ordering =['-id']
    
    def __str__(self):
        return self.judul