# Generated by Django 4.1.6 on 2023-02-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=100)),
                ('PRDDescription', models.TextField(max_length=300)),
                ('PRDPrice', models.IntegerField(blank=True, null=True)),
                ('PRDCost', models.IntegerField(blank=True, null=True)),
                ('PRDTime_created', models.DateTimeField()),
            ],
        ),
    ]