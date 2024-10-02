# Generated by Django 5.1.1 on 2024-09-26 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0007_rename_user_customer_alter_invite_invite_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='invite_code',
            field=models.CharField(default='UYCI8ACXIS', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='invite_expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 9, 53, 30, 564328)),
        ),
    ]
