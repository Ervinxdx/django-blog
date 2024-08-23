from django import forms
from blogs.models import Blog, Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__' #TODOS LOS CAMPOS PARA EL FORMULARIO
        
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['author', 'slug']
        # fields = ('title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')
        
    
