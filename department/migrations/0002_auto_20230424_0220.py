# Generated by Django 3.1 on 2023-04-24 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='Code',
            new_name='code',
        ),
    ]
