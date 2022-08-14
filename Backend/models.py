from django.db import models
from django.db.models.base import Model

# Create your models here.
class HomePage(models.Model):
    id = models.AutoField
    home_title = models.CharField(max_length=30, default="CodeWithSujay")
    home_subtitle = models.CharField(max_length=500, default="Professional Website")
    tech_desc = models.TextField(max_length=5000, default="No Description Available")
    total_student = models.IntegerField(default=0)
    total_course = models.IntegerField(default=0)
    total_review = models.IntegerField(default=0)
    video_desc = models.TextField(max_length=5000)
    video_url = models.CharField(max_length=100, default="")


    def __str__(self):
        return "HomePage"


class ClientReview(models.Model):
    id = models.AutoField
    client_img = models.CharField(max_length=200)
    client_title = models.CharField(max_length=50)
    client_desc = models.TextField(max_length=5000)

    def __str__(self):
        return "ClientReview"


class Chart(models.Model):
    id = models.AutoField
    Technology = models.CharField(max_length=25)
    Projects = models.IntegerField(default=0)

    def __str__(self):
        return "Chart"


class Contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return "Contact"

# id`, `short_title`, `short_desc`, `small_img`, `long_title`, `long_desc`, `total_duration`, `total_lecture`, `total_student`, `skill_all`, `video_url`
class Courses(models.Model):
    id = models.AutoField
    short_title = models.CharField(max_length=30)
    short_desc = models.CharField(max_length=200)
    small_img = models.CharField(max_length=200)
    long_title = models.CharField(max_length=100)
    long_desc = models.TextField(max_length=5000)
    total_duration = models.IntegerField(default=0)
    total_lecture = models.IntegerField(default=0)
    total_student = models.IntegerField(default=0)
    skill_all = models.CharField(max_length=200)
    video_url = models.CharField(max_length=300)

    def __str__(self):
        return "Course"

# (`id`, `address`, `email`, `phone`, `github`, `linkedin`, `codepen`, `footer_credit`, `created_at`,
class Footer(models.Model):
    id = models.AutoField
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    github = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    codepen = models.CharField(max_length=200)
    footer_credit = models.CharField(max_length=300)

    def __str__(self):
        return "Footer"

# `id`, `about`, `refund`, `terms`, `privacy`, `created_at`, `u
class Information(models.Model):
    id = models.AutoField
    about = models.TextField(max_length=2000)
    refund = models.TextField(max_length=20000)
    terms = models.TextField(max_length=20000)
    privacy = models.TextField(max_length=20000)

    def __str__(self):
        return "Information"


# `projects` (`id`, `img_one`, `img_two`, `project_name`, `project_desc`, `project_features`, `live_preview`, `created
class Project(models.Model):
    id = models.AutoField
    img_one = models.CharField(max_length=200)
    img_two = models.CharField(max_length=200)
    project_name = models.CharField(max_length=100)
    project_desc = models.TextField(max_length=20000)
    project_features = models.TextField(max_length=2000)
    live_preview = models.TextField(max_length=2000)


    def __str__(self):
        return "Project"


# services` (`id`, `service_name`, `service_desc`, `service_logo`, `created
class Service(models.Model):
    id = models.AutoField
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField(max_length=20000)
    service_logo = models.CharField(max_length=200)

    def __str__(self):
        return "Service"


