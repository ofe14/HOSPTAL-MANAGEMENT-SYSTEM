# Generated by Django 4.2.1 on 2023-05-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0016_alter_communication_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
