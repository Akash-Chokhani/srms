# Generated by Django 4.2 on 2023-04-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_studies_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
