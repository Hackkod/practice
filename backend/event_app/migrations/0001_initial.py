# Generated by Django 5.0.6 on 2024-07-08 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anket_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('Практика', 'Практика'), ('Стажировка', 'Стажировка')], max_length=20)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_mentor', to='anket_app.mentoranket')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_student', to='anket_app.studentanket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('Договор', 'Договор'), ('Штаб', 'Штаб')], max_length=20)),
                ('position', models.CharField(max_length=1024)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_mentor', to='anket_app.mentoranket')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_student', to='anket_app.studentanket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
