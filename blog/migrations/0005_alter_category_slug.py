# Generated by Django 3.2.9 on 2023-11-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20231114_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]