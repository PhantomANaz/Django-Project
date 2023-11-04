# Generated by Django 4.2.7 on 2023-11-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockMarketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_code', models.CharField(max_length=100)),
                ('high', models.CharField(max_length=100)),
                ('low', models.CharField(max_length=100)),
                ('open', models.CharField(max_length=100)),
                ('close', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentData',
        ),
    ]