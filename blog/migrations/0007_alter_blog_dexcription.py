# Generated by Django 3.2.9 on 2023-12-10 17:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dexcription',
            field=ckeditor.fields.RichTextField(),
        ),
    ]