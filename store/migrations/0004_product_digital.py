# Generated by Django 3.0.8 on 2020-07-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200709_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
