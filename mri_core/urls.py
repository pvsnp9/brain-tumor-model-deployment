from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('operation/', views.operation, name='operation'),
    path('predict-show/<str:image_key>', views.predict_show, name='predict_show'),
    path('upload-file', views.upload_file, name='upload-file'),
    path('about/', views.about, name='about')
]