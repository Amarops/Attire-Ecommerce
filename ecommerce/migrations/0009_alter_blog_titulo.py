# Generated by Django 4.1.2 on 2023-07-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_alter_blog_imagen_alter_blog_texto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=90, verbose_name='Título'),
        ),
    ]
