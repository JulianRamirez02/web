from django.contrib import admin

from institucion.models import complejo_deportivo,Escuela,Profesores,Usuario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Escuela)
admin.site.register(Profesores)
admin.site.register(complejo_deportivo)