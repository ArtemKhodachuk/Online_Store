# Generated by Django 4.1.5 on 2023-04-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
