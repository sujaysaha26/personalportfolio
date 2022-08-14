# Generated by Django 3.1.6 on 2022-01-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_img', models.ImageField(upload_to='')),
                ('client_title', models.CharField(max_length=50)),
                ('client_desc', models.TextField(max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tech_desc',
            field=models.TextField(default='No Description Available', max_length=5000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='video_desc',
            field=models.TextField(max_length=5000),
        ),
    ]
