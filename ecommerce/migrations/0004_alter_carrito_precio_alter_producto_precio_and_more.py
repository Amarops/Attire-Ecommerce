# Generated by Django 4.1.2 on 2023-07-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_producto_valoracion_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='valoracion',
            field=models.IntegerField(),
        ),
    ]