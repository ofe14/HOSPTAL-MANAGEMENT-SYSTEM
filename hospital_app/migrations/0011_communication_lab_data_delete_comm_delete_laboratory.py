# Generated by Django 4.2.1 on 2023-05-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0010_rename_lab_laboratory'),
    ]

    operations = [
        migrations.CreateModel(
            name='communication',
            fields=[
                ('sender', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('receiver', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('file', models.FileField(default='no file', upload_to='files/')),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='lab_data',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=100)),
                ('reciever', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/')),
                ('time', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'lab',
            },
        ),
        migrations.DeleteModel(
            name='comm',
        ),
        migrations.DeleteModel(
            name='laboratory',
        ),
    ]
