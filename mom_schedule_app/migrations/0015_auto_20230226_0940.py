# Generated by Django 3.2.17 on 2023-02-26 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mom_schedule_app', '0014_auto_20230225_1802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mom_task',
            options={'ordering': ['start_time']},
        ),
        migrations.RemoveField(
            model_name='mom_task',
            name='date',
        ),
    ]
