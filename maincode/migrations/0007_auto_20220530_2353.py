# Generated by Django 3.2.5 on 2022-05-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincode', '0006_auto_20220530_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='resgister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100000)),
                ('email', models.EmailField(max_length=254)),
                ('passwords', models.CharField(default=' ', max_length=100000)),
            ],
        ),
        migrations.AlterField(
            model_name='mydata',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
