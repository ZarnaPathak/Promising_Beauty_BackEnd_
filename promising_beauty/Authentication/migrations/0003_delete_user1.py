# Generated by Django 4.1.5 on 2023-01-17 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_user1_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user1',
        ),
    ]
