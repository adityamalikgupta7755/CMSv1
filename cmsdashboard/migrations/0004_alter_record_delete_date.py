# Generated by Django 4.1.1 on 2022-09-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsdashboard', '0003_rename_date_record_delete_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record_delete',
            name='date',
            field=models.CharField(max_length=120),
        ),
    ]