# Generated by Django 4.1.1 on 2022-09-29 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_contacts_clients_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='clients_email',
        ),
    ]
