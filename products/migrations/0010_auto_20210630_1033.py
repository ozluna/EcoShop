# Generated by Django 3.2 on 2021-06-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_productreview_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review_date',
            field=models.DateField(default=None),
        ),
    ]
