# Generated by Django 3.2 on 2021-07-11 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]