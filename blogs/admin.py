from django.contrib import admin

from blogs.models import Category

from blogs.models import Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'category', 'status' ,'is_featured')
    search_fields = ('id' , 'title' , 'category__category_name' , 'status')
    list_editable = ('is_featured',)
class CategoryAdmin(admin.ModelAdmin): #ASI PODEMOS ANADIR UN BUSCADOR
    search_fields = ('category_name',)


# Register your models here.

admin.site.register(Category, CategoryAdmin) #NO OLVIDAR REGISTRAR TAMBIEN EL MODELO CATEGORY
admin.site.register(Blog,BlogAdmin)


#ASI SE REGISTRA ()arriba)
