# Generated by Django 5.1.4 on 2025-01-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='test1'),
            preserve_default=False,
        ),
    ]
