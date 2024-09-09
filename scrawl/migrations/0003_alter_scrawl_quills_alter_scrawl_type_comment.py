# Generated by Django 5.0.7 on 2024-08-03 20:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrawl', '0002_scrawl'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrawl',
            name='quills',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scrawl',
            name='type',
            field=models.CharField(choices=[('Poem', 'Poem'), ('Lyrics', 'Lyrics'), ('Excerpt', 'Excerpt'), ('Drabble', 'Drabble')], max_length=10),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('quills', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scrawl', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='scrawl.scrawl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]