# Generated by Django 3.2.25 on 2024-03-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default="2023-04-3"),
            preserve_default=False,
        ),
    ]
