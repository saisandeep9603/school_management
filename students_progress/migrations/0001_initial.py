# Generated by Django 4.2 on 2023-04-26 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0002_alter_staff_name_alter_staff_files_staff_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_names', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='students_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.students')),
                ('sub_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students_progress.subjects')),
            ],
        ),
    ]
