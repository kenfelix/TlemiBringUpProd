# Generated by Django 4.0.6 on 2022-07-27 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_remove_department_unique_member_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='department',
            name='unique_member',
        ),
    ]
