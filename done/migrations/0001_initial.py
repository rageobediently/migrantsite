# Generated by Django 2.2.3 on 2019-08-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThisDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameser', models.CharField(max_length=100)),
                ('done', models.BooleanField()),
            ],
        ),
    ]
