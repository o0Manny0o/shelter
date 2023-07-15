# Generated by Django 4.2.2 on 2023-07-13 04:54

import cms_public.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms_public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('level', models.IntegerField(default=0)),
                ('title', models.CharField(default='Title', max_length=50)),
                ('layout', models.ForeignKey(default=cms_public.models.Layout.get_default_pk, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='pages', to='cms_public.layout')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='cms.page')),
            ],
        ),
        migrations.CreateModel(
            name='PagePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('content', models.TextField(max_length=2000)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='cms.page')),
            ],
        ),
    ]