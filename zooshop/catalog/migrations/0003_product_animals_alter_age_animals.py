# Generated by Django 4.1.7 on 2023-03-15 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_age_animals'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='animals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalog.animal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='age',
            name='animals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.animal'),
        ),
    ]