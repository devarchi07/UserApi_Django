# Generated by Django 3.2.3 on 2021-05-29 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gstin', models.CharField(max_length=30, unique=True)),
                ('shop_address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]
