# Generated by Django 4.1.13 on 2023-11-17 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='message',
            new_name='msg',
        ),
        migrations.RenameField(
            model_name='blogmodel',
            old_name='userid',
            new_name='user_id',
        ),
    ]
