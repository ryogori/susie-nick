# Generated by Django 4.0.3 on 2022-07-18 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muscle_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_list',
            old_name='user_name',
            new_name='username',
        ),
    ]