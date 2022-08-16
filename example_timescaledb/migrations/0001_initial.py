# Generated by Django 4.1 on 2022-08-16 11:35

from django.db import migrations, models
import timescale.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArcReactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', timescale.db.models.fields.TimescaleDateTimeField(interval='1 day')),
                ('voltage', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]