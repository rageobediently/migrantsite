# Generated by Django 2.2.3 on 2019-08-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesss',
            name='price',
            field=models.CharField(default=100, max_length=5),
            preserve_default=False,
        ),
    ]
