# Generated by Django 4.2.1 on 2023-05-25 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0012_alter_communication_table_alter_lab_data_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='communication',
            table='messages',
        ),
        migrations.AlterModelTable(
            name='lab_data',
            table='lab',
        ),
    ]
