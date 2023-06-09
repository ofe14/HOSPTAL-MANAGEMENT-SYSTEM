# Generated by Django 4.2.1 on 2023-05-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='lab_result',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
                'db_table': 'lab_result',
            },
        ),
    ]
