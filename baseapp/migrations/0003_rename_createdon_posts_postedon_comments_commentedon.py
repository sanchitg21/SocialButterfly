# Generated by Django 4.0.3 on 2022-04-12 14:17

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_posts_createdon_alter_userdetails_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='CreatedOn',
            new_name='PostedOn',
        ),
        migrations.AddField(
            model_name='comments',
            name='CommentedOn',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
