# Generated by Django 5.0.1 on 2024-01-15 17:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_likepost_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
