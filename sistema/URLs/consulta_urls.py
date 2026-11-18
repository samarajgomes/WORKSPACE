from django.urls import path
from sistema.VIEWS import consulta_view

urlpatterns = [
    path('consulta/', consulta_view), 
]