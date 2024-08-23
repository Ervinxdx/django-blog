from django.contrib.auth.forms import UserCreationForm
#Reutilizar el form para crean un usuario.
#Django.
from django.contrib.auth.models import User
#Para crear un usuario pero reuzando los que nos brinda
#Django.


class RegistrarionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','password1','password2') #Elegir como se registrara el usuario.

    def save(self,commit=True):
        user= super(RegistrarionForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True #PARA QUE PUEDA INICIAR SESION EN EL PANEL DE DMINISTRACION
        
        
        if commit:
            user.save()
            
        return user