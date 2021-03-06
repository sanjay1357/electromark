# Generated by Django 3.1.3 on 2020-11-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0005_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('tablename', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30, null=True)),
                ('productid', models.IntegerField()),
                ('tracking', models.BigIntegerField(unique=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('times', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
