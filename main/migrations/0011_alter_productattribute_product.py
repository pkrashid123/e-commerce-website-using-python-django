# Generated by Django 4.0.4 on 2022-05-20 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_productattribute_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(default='NaN', on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]
