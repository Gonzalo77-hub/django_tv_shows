from django.urls import path
from . import views
urlpatterns = [
    path('', views.redir),
    path('Shows', views.index),
    path('Shows/create', views.crear),
    path('Shows/New', views.second),
    path('Shows/<int:val>', views.info_show),
    path('Shows/<int:val>/edit', views.edit_show),
    path('Shows/editar', views.edit),
    path('Shows/<int:val>/borrar', views.delete),

]
