# Generated by Django 5.0.4 on 2024-04-06 22:49

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('responsibilities', ckeditor.fields.RichTextField(verbose_name='Responsibilities')),
                ('requirements', ckeditor.fields.RichTextField(verbose_name='Requirements')),
                ('conditions', ckeditor.fields.RichTextField(verbose_name='Conditions')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'vacancy',
                'verbose_name_plural': 'vacancies',
            },
        ),
    ]
