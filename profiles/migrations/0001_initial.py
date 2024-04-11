# Generated by Django 3.2.25 on 2024-04-08 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('surname', models.CharField(max_length=254)),
                ('address_1', models.CharField(max_length=254)),
                ('address_2', models.CharField(max_length=254)),
                ('address_3', models.CharField(max_length=254)),
                ('address_country', models.CharField(max_length=254)),
                ('address_postcode', models.CharField(max_length=254)),
                ('newsletter_update', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]