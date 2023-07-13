from django.urls import path
from . import views

urlpatterns=[
    path('enquiry-form/', views.registration, name="enquiry"),
    path("", views.index, name="index"),
    path('download/', views.download_file, name="download_file"),
    path('downloadenquiry/', views.downloadenquiry, name="downloadenquiry"),
    path('contact/', views.contact, name="contact")
    #  path('download/<str:file_path>/', views.download_file, name='download_file'),
]