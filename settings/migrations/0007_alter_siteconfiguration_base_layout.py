# Generated by Django 4.2.2 on 2023-10-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_siteconfiguration_base_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='base_layout',
            field=models.CharField(choices=[('side_navigation.html', 'Side Navigation')], default='side_navigation.html'),
        ),
    ]