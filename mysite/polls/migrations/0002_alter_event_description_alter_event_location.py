# Generated by Django 5.0.1 on 2024-02-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]
