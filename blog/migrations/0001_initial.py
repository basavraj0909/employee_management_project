# Generated by Django 4.2.15 on 2024-09-01 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 9, 1, 17, 28, 55, 604824, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
