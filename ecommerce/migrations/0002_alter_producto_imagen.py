# Generated by Django 4.1.2 on 2023-07-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]
