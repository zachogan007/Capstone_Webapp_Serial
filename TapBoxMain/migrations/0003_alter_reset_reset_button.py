# Generated by Django 3.2.7 on 2022-11-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapBoxMain', '0002_reset_reset_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reset',
            name='reset_button',
            field=models.CharField(max_length=200),
        ),
    ]
