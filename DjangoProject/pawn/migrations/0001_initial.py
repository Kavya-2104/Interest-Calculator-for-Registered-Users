# Generated by Django 4.1.7 on 2023-03-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('amount', models.FloatField()),
                ('interest', models.FloatField()),
                ('month', models.IntegerField()),
                ('phnno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('collateral', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
    ]
