# Generated by Django 4.0.4 on 2022-05-30 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_banner_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specs',
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]