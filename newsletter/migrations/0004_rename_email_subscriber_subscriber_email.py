# Generated by Django 3.2 on 2022-08-30 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_subscriberemail_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='email',
            new_name='subscriber_email',
        ),
    ]
