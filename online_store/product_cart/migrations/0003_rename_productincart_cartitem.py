# Generated by Django 4.1.5 on 2023-04-17 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productimage_image'),
        ('product_cart', '0002_productincart_delete_productcart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductInCart',
            new_name='CartItem',
        ),
    ]
