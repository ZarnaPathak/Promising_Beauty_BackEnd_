# Generated by Django 4.1.5 on 2023-01-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('dbg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dbg_fname', models.CharField(max_length=50)),
                ('dbg_lname', models.CharField(max_length=50)),
                ('dbg_password', models.CharField(max_length=20)),
                ('dbg_email', models.CharField(max_length=30)),
                ('dbg_phoneno', models.IntegerField()),
                ('dbg_gender', models.CharField(max_length=15)),
                ('dbg_img', models.CharField(max_length=50)),
                ('dbg_adharcard', models.IntegerField()),
                ('dbg_address', models.CharField(max_length=100)),
            ],
        ),
    ]
