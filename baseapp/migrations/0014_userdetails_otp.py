# Generated by Django 4.0.5 on 2022-06-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0013_remove_userdetails_counter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
