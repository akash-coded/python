# Generated by Django 2.0.2 on 2018-03-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=100)),
            ],
        ),
    ]