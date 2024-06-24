# Generated by Django 5.0.6 on 2024-06-24 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketApp', '0002_alter_mentoranket_hard_skills_id_and_more'),
        ('eventApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practiceorinternship',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pi_mentor', to='anketApp.mentoranket'),
        ),
        migrations.AlterField(
            model_name='practiceorinternship',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pi_student', to='anketApp.studentanket'),
        ),
    ]
