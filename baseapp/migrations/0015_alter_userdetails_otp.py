# Generated by Django 4.0.5 on 2022-06-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_userdetails_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='otp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]