# Generated by Django 3.1.6 on 2022-01-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_auto_20220102_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='client_img',
            field=models.CharField(max_length=100),
        ),
    ]