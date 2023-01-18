# Generated by Django 4.1.5 on 2023-01-18 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customizationhome',
            fields=[
                ('custm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('custm_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='hoop',
            fields=[
                ('hoop_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hoop_layout', models.IntegerField()),
                ('hoop_name1', models.CharField(max_length=100)),
                ('hoop_name2', models.CharField(max_length=100)),
                ('hoop_date', models.DateField()),
                ('hoop_msg', models.TextField(max_length=30)),
                ('custm_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='customization.customizationhome')),
            ],
        ),
    ]
