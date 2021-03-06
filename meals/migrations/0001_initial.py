# Generated by Django 3.0.7 on 2020-06-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealName', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=50)),
                ('noOfPeople', models.IntegerField()),
                ('prepTime', models.IntegerField()),
                ('image', models.ImageField(upload_to='Meals/')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
            },
        ),
    ]
