# Generated by Django 5.0.7 on 2024-08-05 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrawl', '0005_remove_scrawl_quills_alter_scrawl_saved_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrawl',
            old_name='quills',
            new_name='liked_by',
        ),
    ]