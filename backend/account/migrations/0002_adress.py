# Generated by Django 3.1.2 on 2020-10-06 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_first_name', models.CharField(max_length=100)),
                ('adress_last_name', models.CharField(max_length=100)),
                ('adress_phone', models.CharField(max_length=30, verbose_name='phone')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('adresss', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
