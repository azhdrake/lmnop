# Generated by Django 2.1.11 on 2020-04-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='posted_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
