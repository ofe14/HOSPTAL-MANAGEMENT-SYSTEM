# Generated by Django 4.2.1 on 2023-05-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0019_register_allergies_register_chronic_illness_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='current_meds',
        ),
        migrations.AlterField(
            model_name='register',
            name='identification',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
