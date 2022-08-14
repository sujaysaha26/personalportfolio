from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name="HomePage"),
    path('clientreview/', views.clientreview, name="ClientReview"),
    path('chart/', views.chart, name="Chart"),
    path('contact/', views.contact, name="Contact"),
    path('course/', views.course, name="Course"),
    path('footer/', views.footer, name="Footer"),
    path('information/', views.information, name="Infomation"),
    path('project/', views.project, name="Project"),
    path('service/', views.service, name="Service"),
]