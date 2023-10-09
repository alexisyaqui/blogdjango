from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)   #titulo
    slug = models.SlugField(unique=True) #etiqueta en la url
    overview = models.TextField()  #descripcion
    date_create = models.DateTimeField(auto_now_add=True) #para que se cree el registro
    content = models.TextField() # contenido
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT) #recomando para hacer relacion con el usuario
    categories = models.ManyToManyField('Category')
    features = models.BooleanField(default=False) #desctacado
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)#imagen
    pub_date = models.DateTimeField(default=timezone.now)
    def get_absolute_url(self):
        return reverse("blogs:post_detalle", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['date_create']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("blogs:category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
