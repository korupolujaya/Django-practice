# Generated by Django 5.0.3 on 2024-03-12 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='pub_date',
        ),
    ]
