# Generated by Django 3.2.5 on 2022-05-28 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maincode', '0002_addprojects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addprojects',
            old_name='tech',
            new_name='techdata',
        ),
    ]
