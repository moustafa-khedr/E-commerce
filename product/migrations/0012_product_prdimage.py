# Generated by Django 4.1.6 on 2023-02-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_prdslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='image'),
        ),
    ]