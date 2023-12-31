# Generated by Django 5.0 on 2023-12-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=200, null=True, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(null=True, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(null=True, verbose_name='main text'),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='article name'),
        ),
    ]
