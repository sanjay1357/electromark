# Generated by Django 3.1.3 on 2020-11-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20201130_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='category',
            field=models.CharField(choices=[('COMPUTERS', 'COMPUTERS'), ('LAPTOPS', 'LAPTOPS')], default='COMPUTERS', max_length=10),
        ),
        migrations.AlterField(
            model_name='pc',
            name='pcharddisk',
            field=models.IntegerField(choices=[('0', 'NIL'), ('32', '32GB'), ('250', '250GB'), ('320', '320GB'), ('500', '500GB'), ('1', '1TB'), ('2', '2TB'), ('3', '3TB'), ('4', '4TB')], default='0'),
        ),
        migrations.AlterField(
            model_name='pc',
            name='pcram',
            field=models.IntegerField(choices=[('2', '2GB'), ('4', '4GB'), ('6', '6GB'), ('8', '8GB'), ('16', '16GB')], default='2'),
        ),
        migrations.AlterField(
            model_name='pc',
            name='pcssd',
            field=models.IntegerField(choices=[('0', 'NIL'), ('8', '8GB'), ('128', '128GB'), ('256', '256GB'), ('512', '512GB'), ('500', '500GB'), ('1', '1TB'), ('2', '2TB')], default='0'),
        ),
    ]