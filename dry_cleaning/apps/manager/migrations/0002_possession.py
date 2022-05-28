# Generated by Django 4.0.3 on 2022-05-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50)),
                ('type', models.TextField(blank=True, max_length=50)),
                ('service', models.TextField(blank=True, max_length=50)),
                ('chemical', models.TextField(blank=True, max_length=50)),
                ('cost', models.TextField(blank=True, max_length=50)),
                ('hour', models.TextField(blank=True, max_length=50)),
                ('date', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]