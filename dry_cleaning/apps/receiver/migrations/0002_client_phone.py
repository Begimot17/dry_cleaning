# Generated by Django 4.0.3 on 2022-05-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.TextField(null=True),
        ),
    ]