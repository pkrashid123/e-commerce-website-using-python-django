# Generated by Django 4.0.4 on 2022-05-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_productattribute_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='media/brand_img/'),
        ),
    ]
