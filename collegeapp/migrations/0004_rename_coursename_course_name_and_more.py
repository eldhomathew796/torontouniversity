# Generated by Django 4.1.3 on 2023-09-22 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0003_studentdetails_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='coursename',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='departmentname',
            new_name='name',
        ),
    ]
