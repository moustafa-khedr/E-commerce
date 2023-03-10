# Generated by Django 4.1.6 on 2023-02-15 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATDescription',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATImage',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATName',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name=' Main Category'),
        ),
    ]
