# Generated by Django 4.1 on 2022-09-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ac_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(default='default.jpg', upload_to='ACM/Academies')),
                ('official_web', models.CharField(max_length=150)),
            ],
        ),
    ]
