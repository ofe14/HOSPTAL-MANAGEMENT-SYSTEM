# Generated by Django 4.2.1 on 2023-05-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoinment',
            fields=[
                ('patient_id', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100, primary_key=True, serialize=False)),
                ('time', models.TimeField(max_length=6)),
                ('add_info', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'appointments',
            },
        ),
        migrations.CreateModel(
            name='doc_sess',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('cheif_complaint', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'doc_sess',
            },
        ),
        migrations.CreateModel(
            name='patientlog',
            fields=[
                ('patient_id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('activity', models.CharField(max_length=150)),
                ('additional_info', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'patient_log',
            },
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('reg_date', models.DateField(max_length=100)),
                ('firstname', models.CharField(max_length=200)),
                ('middlename', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('dateofbirth', models.DateField(max_length=100)),
                ('marital_status', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('emg_name', models.CharField(max_length=200)),
                ('emg_address', models.CharField(max_length=200)),
                ('emg_phone', models.CharField(max_length=200)),
                ('emg_state', models.CharField(max_length=200)),
                ('payment', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
        migrations.CreateModel(
            name='staffs',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='vital',
            fields=[
                ('date', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('blood_pressure', models.CharField(max_length=100)),
                ('sugar_level', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('heart_rate', models.CharField(max_length=100)),
                ('temperature', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('respiration', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vitals',
            },
        ),
    ]