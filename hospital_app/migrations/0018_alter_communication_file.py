# Generated by Django 4.2.1 on 2023-05-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0017_alter_communication_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]