from django.urls import path
from .views import homeview,uploadview,photolist

urlpatterns = [
    path('home/',homeview,name='home'),
    path('upload/',uploadview,name='upload'),
    path('photolist/',photolist,name='photolist'),

]