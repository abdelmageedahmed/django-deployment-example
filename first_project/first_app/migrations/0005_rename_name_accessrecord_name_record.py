# Generated by Django 3.2.5 on 2022-08-11 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_alter_accessrecord_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='name',
            new_name='name_record',
        ),
    ]
