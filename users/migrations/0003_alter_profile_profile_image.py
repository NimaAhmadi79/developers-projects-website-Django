# Generated by Django 4.1.6 on 2023-02-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default.jpg', null=True, upload_to='profiles/'),
        ),
    ]
