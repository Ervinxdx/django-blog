from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#makemigrations hacer migraciones,aun no genera la tabla
#migrate =  Para crear la tabla
STATUS_CHOICES = (
    ("Draft", 'Draft'),
    ("Published",'Published')
)
class Category(models.Model):
    category_name = models.CharField(max_length=50 ,unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)
    #CORREGIR EL NOMBRE
    class Meta:
        verbose_name_plural = 'categories'
    #COLOCAR UN NOMBRE EN LAS CATEGORIAS
    def __str__(self):
        return self.category_name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body= models.TextField(max_length=2000)
    status = models.TextField( max_length= 20 ,choices=STATUS_CHOICES,  default="Draft")
    is_featured = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title