# Generated by Django 4.1.6 on 2023-02-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_image',
            field=models.ImageField(blank=True, default='IMG_20201113_230341.jpg', null=True, upload_to=''),
        ),
    ]
