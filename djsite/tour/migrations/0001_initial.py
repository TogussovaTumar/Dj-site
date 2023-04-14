# Generated by Django 4.2 on 2023-04-12 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Header')),
                ('content', models.TextField(blank=True, verbose_name='Information')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('price', models.CharField(max_length=255, verbose_name='Price')),
                ('country', models.TextField(blank=True, verbose_name='Country')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('is_published', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tour.category', verbose_name='Region')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
                'ordering': ['-time_create', 'name'],
            },
        ),
    ]
