# Generated by Django 2.2 on 2019-09-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogName', models.CharField(max_length=200)),
                ('dogBreed', models.CharField(max_length=200)),
                ('dogColor', models.CharField(max_length=200)),
                ('dogGender', models.CharField(max_length=200)),
            ],
        ),
    ]
