# Generated by Django 4.1.5 on 2023-03-27 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productpresent_price'),
        ('product_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_incart', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productpresent')),
            ],
        ),
        migrations.DeleteModel(
            name='Productcart',
        ),
    ]
