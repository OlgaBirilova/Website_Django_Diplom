# Generated by Django 4.1.7 on 2023-03-26 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
