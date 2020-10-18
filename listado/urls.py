from django.urls import path
from . import views
from listado.views import listado


urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('leer', listado.as_view(template_name = "listado.html"), name='leer'),
    
    
]