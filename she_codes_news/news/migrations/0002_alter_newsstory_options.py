# Generated by Django 3.2.5 on 2021-08-24 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['pub_date']},
        ),
    ]
