# Generated by Django 2.2 on 2020-03-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user_man',
            new_name='user',
        ),
    ]
