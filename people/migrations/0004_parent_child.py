# Generated by Django 4.2.6 on 2023-10-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_remove_parent_child_alter_parent_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='child',
            field=models.ManyToManyField(related_name='child', to='people.person'),
        ),
    ]
