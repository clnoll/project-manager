# Generated by Django 2.0.5 on 2018-06-21 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0004_taskitem_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
    ]
