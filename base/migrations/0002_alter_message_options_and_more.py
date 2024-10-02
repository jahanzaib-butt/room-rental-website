# Generated by Django 5.1.1 on 2024-10-02 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated',
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='base.room'),
        ),
    ]