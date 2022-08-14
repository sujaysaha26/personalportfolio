from django.shortcuts import render
from django.http import HttpResponse

from .models import Chart, Contact, Courses, Footer, HomePage, ClientReview, Information, Project, Service
from .serializers import HomePageSerializer,ClientReviewSerializer, ChartSerializer, ContactSerializer, CourseSerializer, FooterSerialzer, InformationSerialzer, ProjectSerialzer, ServiceSerialzer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# class HomePageCreate(generics.ListCreateAPIView):
#     queryset = HomePage.objects.all()
#     serializer_class = LeadSerializer



@api_view(['GET'])
def ReactPage(request):
    api_urls = {
        'HomePage': '/homepage',
        'ClientReview': '/clientreview',
        'Chart': '/chart',
        'Contact': '/contact',
        'Course': '/course',
        'Footer': '/footer',
        'Information': '/information',
        'Project': '/project',
        'Services': '/services',
    }

    return Response(api_urls)


@api_view(['GET'])
def homepage(request):
    homepage = HomePage.objects.all()
    serializer = HomePageSerializer(homepage, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def clientreview(request):
    clientreviews = ClientReview.objects.all()
    serializer = ClientReviewSerializer(clientreviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def chart(request):
    charts = Chart.objects.all()
    serializer = ChartSerializer(charts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def contact(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course(request):
    courses = Courses.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def footer(request):
    footerdetail = Footer.objects.all()
    serialzer = FooterSerialzer(footerdetail, many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def information(request):
    informationall = Information.objects.all()
    serailzer = InformationSerialzer(informationall, many=True)
    return Response(serailzer.data)

@api_view(['GET'])
def project(request):
    projectdetails = Project.objects.all()
    serailzer = ProjectSerialzer(projectdetails, many=True)
    return Response(serailzer.data)

@api_view(['GET'])
def service(request):
    servicedetails = Service.objects.all()
    serailzer = ServiceSerialzer(servicedetails, many=True)
    return Response(serailzer.data)