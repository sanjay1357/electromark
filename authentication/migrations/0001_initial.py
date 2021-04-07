# Generated by Django 3.1.3 on 2020-11-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('birthday', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('passw', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=50, null=True)),
                ('address1', models.CharField(max_length=500, null=True)),
                ('address2', models.CharField(max_length=500, null=True)),
                ('landmark', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('address_type', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
