# Generated by Django 4.0.3 on 2022-05-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
