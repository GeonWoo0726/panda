# Generated by Django 3.1.3 on 2023-11-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0010_auto_20231120_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='registerStatus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
