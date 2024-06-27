# Generated by Django 4.2.2 on 2023-10-23 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_public', '0002_alter_section_unique_together'),
        ('cms', '0005_alter_page_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='layout',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='pages', to='cms_public.layout'),
        ),
    ]