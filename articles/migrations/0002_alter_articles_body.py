# Generated by Django 4.1.5 on 2023-01-30 06:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]