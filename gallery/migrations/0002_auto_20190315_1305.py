# Generated by Django 2.1.7 on 2019-03-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
