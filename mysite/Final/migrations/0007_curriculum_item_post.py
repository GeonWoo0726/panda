# Generated by Django 3.1.3 on 2023-11-20 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0006_auto_20231117_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]