from django.urls import path
from institucion import views

urlpatterns = [
    path('',views.index,name="Index"),
    path('other_page/',views.other_page,name="Otra Pagina"),
]