# Generated by Django 4.1.3 on 2022-12-18 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='age',
            new_name='mobile_number',
        ),
    ]
