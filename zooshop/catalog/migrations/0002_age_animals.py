# Generated by Django 4.1.7 on 2023-03-15 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='age',
            name='animals',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.animal'),
        ),
    ]