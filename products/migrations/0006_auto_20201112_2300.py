# Generated by Django 3.1.3 on 2020-11-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201109_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='appliances',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pc',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tv',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
