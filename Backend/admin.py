from django.contrib import admin
from .models import Chart, ClientReview, Contact, Courses, Footer, HomePage, Information, Project, Service

# Register your models here.
admin.site.register(HomePage)
admin.site.register(ClientReview)
admin.site.register(Service)
admin.site.register(Footer)
admin.site.register(Chart)
admin.site.register(Contact)
admin.site.register(Courses)
admin.site.register(Information)
admin.site.register(Project)