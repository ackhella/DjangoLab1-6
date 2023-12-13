# Generated by Django 5.0 on 2023-12-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]