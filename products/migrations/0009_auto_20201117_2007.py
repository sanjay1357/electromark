# Generated by Django 3.1.3 on 2020-11-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201116_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliances',
            name='appcapacity',
            field=models.FloatField(),
        ),
    ]
