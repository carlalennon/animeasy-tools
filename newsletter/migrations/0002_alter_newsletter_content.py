# Generated by Django 5.0.6 on 2024-05-15 00:00
from django.db import migrations, models 


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=models.TextField(),
        ),
    ]
