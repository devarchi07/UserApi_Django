# Generated by Django 3.2.3 on 2021-05-29 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('user_id', models.IntegerField(primary_key=int, serialize=False)),
                ('address', models.TextField()),
                ('phonenumber', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
