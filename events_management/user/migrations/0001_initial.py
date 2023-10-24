# Generated by Django 4.2.6 on 2023-10-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('id_number', models.PositiveIntegerField(max_length=9, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('un_read_messages', models.IntegerField()),
            ],
        ),
    ]
