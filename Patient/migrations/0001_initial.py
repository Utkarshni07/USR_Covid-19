# Generated by Django 3.1.7 on 2021-04-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('DryCough', models.CharField()),
                ('HighFever', models.CharField()),
                ('SoreThroat', models.CharField()),
                ('Difficulty_in_breathing', models.CharField()),
                ('Infected_with_Covid19', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Coviduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=67)),
                ('password', models.CharField(max_length=67)),
                ('username', models.CharField(max_length=89)),
            ],
        ),
    ]
