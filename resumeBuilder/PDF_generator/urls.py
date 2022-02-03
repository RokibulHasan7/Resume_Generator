from django.urls import path
from . import views
from .views import GeneratePDF

urlpatterns = [
    path('resumefill/', views.resumeFill, name='resume_fill'),
    path('resumeview/', views.resumeView, name='resume_view'),
    #path('pdfgen/', GeneratePDF.as_view(), name='gen'),
]