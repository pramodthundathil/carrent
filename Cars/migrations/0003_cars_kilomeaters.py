# Generated by Django 3.2.14 on 2023-02-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0002_auto_20230204_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='Kilomeaters',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
