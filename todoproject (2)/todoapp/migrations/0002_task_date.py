# Generated by Django 4.2.3 on 2023-07-07 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-12-25'),
            preserve_default=False,
        ),
    ]
