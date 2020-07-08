from django.urls import path

from . import views

# polls URLconf (/polls/)
urlpatterns = [
    path('', views.index, name='index')
]
