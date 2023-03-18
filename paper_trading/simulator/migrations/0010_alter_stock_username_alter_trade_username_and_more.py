# Generated by Django 4.1.6 on 2023-03-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0009_remove_stock_user_remove_trade_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='username',
            field=models.CharField(default='kk', max_length=50),
        ),
        migrations.AlterField(
            model_name='trade',
            name='username',
            field=models.CharField(default='kk', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]