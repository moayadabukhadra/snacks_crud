# Generated by Django 4.0.4 on 2022-05-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
