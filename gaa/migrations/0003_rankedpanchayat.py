# Generated by Django 2.0.3 on 2018-03-31 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaa', '0002_remove_panchayat_dev_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankedPanchayat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panchayat', models.CharField(max_length=200)),
                ('dev_index', models.CharField(max_length=200)),
            ],
        ),
    ]
