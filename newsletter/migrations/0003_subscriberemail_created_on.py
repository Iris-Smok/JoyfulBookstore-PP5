# Generated by Django 3.2 on 2022-08-24 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_rename_subscribers_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberemail',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
