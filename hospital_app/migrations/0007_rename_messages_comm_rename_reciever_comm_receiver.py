# Generated by Django 4.2.1 on 2023-05-25 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0006_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='messages',
            new_name='comm',
        ),
        migrations.RenameField(
            model_name='comm',
            old_name='reciever',
            new_name='receiver',
        ),
    ]