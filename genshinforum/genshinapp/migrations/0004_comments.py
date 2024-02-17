# Generated by Django 5.0.1 on 2024-02-08 10:09

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genshinapp', '0003_alter_themes_themeimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('commentcontent', ckeditor.fields.RichTextField()),
                ('comment_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]