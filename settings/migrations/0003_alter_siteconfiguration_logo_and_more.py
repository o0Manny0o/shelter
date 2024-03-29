# Generated by Django 4.2.2 on 2023-08-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_siteconfiguration_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='logo',
            field=models.ImageField(default='./logo.png', help_text='The logo next to the title', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='title',
            field=models.CharField(help_text='Page title displayed at the top of every page', max_length=25),
        ),
    ]
