# Generated by Django 4.2 on 2023-04-12 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_rename_branches_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.branch')),
                ('sub_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.subjects')),
            ],
        ),
    ]
