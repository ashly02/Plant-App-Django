# Generated by Django 4.2.1 on 2023-05-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantdb',
            name='plantimages',
            field=models.ImageField(default='null.jpg', upload_to='image'),
        ),
    ]
