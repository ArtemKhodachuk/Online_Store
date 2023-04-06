# Generated by Django 4.1.5 on 2023-03-27 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='client_info.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Productcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity_incart', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_cart.cart')),
            ],
        ),
    ]