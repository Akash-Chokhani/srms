# Generated by Django 4.2 on 2023-04-12 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_branch_subjects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='code',
            new_name='br_code',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='name',
            new_name='br_name',
        ),
        migrations.RenameField(
            model_name='branch_subjects',
            old_name='branch_code',
            new_name='br_code',
        ),
    ]