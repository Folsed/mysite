# Generated by Django 4.1 on 2022-09-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('lat', models.CharField(max_length=50, verbose_name='Latitude')),
                ('lng', models.CharField(max_length=50, verbose_name='Longitude')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
            ],
        ),
    ]
