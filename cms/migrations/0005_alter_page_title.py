# Generated by Django 4.2.2 on 2023-08-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_alter_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(default='My new page', max_length=50),
        ),
    ]
