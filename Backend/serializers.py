from django.db.models import fields
from rest_framework import serializers
from .models import HomePage, ClientReview, Chart, Contact, Courses, Footer, Information, Project, Service

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'

class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = '__all__'

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class FooterSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

class InformationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'
    
class ProjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ServiceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'