# Generated by Django 4.0.6 on 2022-07-19 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finchcollectordatabase', '0002_feeding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
    ]