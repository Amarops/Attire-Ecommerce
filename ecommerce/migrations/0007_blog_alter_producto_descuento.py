# Generated by Django 4.1.2 on 2023-07-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_alter_producto_descuento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('usuario', models.CharField(max_length=50, verbose_name='Usuario')),
                ('texto', models.CharField(max_length=50, verbose_name='Texto')),
                ('imagen', models.ImageField(null=True, upload_to='ecommerce/static/images', verbose_name='Imagen')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='descuento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
