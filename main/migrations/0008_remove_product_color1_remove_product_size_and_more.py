# Generated by Django 4.0.4 on 2022-05-19 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_specs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.DeleteModel(
            name='color1',
        ),
        migrations.DeleteModel(
            name='size',
        ),
    ]
