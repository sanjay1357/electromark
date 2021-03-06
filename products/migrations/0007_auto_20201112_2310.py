# Generated by Django 3.1.3 on 2020-11-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201112_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='accconnectivity',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='accfeatures',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='accinterfaces',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='acctype',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='appliances',
            name='appfeatures',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='appliances',
            name='apptype',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='appliances',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='color',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='processor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pc',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pc',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='pc',
            name='pcprocessor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tv',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tv',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
