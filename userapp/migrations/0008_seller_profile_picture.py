# Generated by Django 3.2.3 on 2021-05-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_auto_20210530_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='profile_picture',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
