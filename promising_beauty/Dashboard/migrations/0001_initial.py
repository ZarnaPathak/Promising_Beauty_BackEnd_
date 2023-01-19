# Generated by Django 4.1.5 on 2023-01-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]