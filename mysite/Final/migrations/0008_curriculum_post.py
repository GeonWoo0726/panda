# Generated by Django 3.1.3 on 2023-11-20 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0007_curriculum_item_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=50)),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
                ('contents', models.TextField()),
            ],
        ),
    ]
