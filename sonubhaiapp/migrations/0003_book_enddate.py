# Generated by Django 4.0.2 on 2022-04-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sonubhaiapp', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Enddate',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
