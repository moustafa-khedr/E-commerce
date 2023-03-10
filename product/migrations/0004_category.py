# Generated by Django 4.1.6 on 2023-02-15 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=50)),
                ('CATDescription', models.TextField(blank=True, max_length=300, null=True)),
                ('CATImage', models.ImageField(blank=True, null=True, upload_to='category')),
                ('CATParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
