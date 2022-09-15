# Generated by Django 4.1 on 2022-09-15 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicManager', '0001_initial'),
        ('users', '0002_remove_user_academy'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Academy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='AcademicManager.academy'),
        ),
    ]
