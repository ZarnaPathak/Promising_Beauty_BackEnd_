# Generated by Django 4.1.5 on 2023-01-17 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_cat_remove_p_details1_id_p_details1_p_id_subcat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_details1',
            name='subcat_id',
        ),
        migrations.RemoveField(
            model_name='subcat',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='cat',
        ),
        migrations.DeleteModel(
            name='p_details1',
        ),
        migrations.DeleteModel(
            name='subcat',
        ),
    ]
