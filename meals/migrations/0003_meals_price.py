# Generated by Django 3.0.7 on 2020-06-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20200613_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
