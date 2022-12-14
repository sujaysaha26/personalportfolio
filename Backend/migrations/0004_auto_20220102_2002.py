# Generated by Django 3.1.6 on 2022-01-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_auto_20220102_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Technology', models.CharField(max_length=25)),
                ('Projects', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(max_length=30)),
                ('short_desc', models.CharField(max_length=200)),
                ('small_img', models.CharField(max_length=200)),
                ('long_title', models.CharField(max_length=100)),
                ('long_desc', models.TextField(max_length=5000)),
                ('total_duration', models.IntegerField(default=0)),
                ('total_lecture', models.IntegerField(default=0)),
                ('total_student', models.IntegerField(default=0)),
                ('skill_all', models.CharField(max_length=200)),
                ('video_url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('github', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
                ('codepen', models.CharField(max_length=200)),
                ('footer_credit', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=2000)),
                ('refund', models.TextField(max_length=20000)),
                ('terms', models.TextField(max_length=20000)),
                ('privacy', models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_one', models.CharField(max_length=200)),
                ('img_two', models.CharField(max_length=200)),
                ('project_name', models.CharField(max_length=100)),
                ('project_desc', models.TextField(max_length=20000)),
                ('project_features', models.TextField(max_length=2000)),
                ('live_preview', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_desc', models.TextField(max_length=20000)),
                ('service_logo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='clientreview',
            name='client_img',
            field=models.CharField(max_length=200),
        ),
    ]
