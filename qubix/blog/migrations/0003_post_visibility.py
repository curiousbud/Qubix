# Generated by Django 5.2.4 on 2025-07-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends Only'), ('private', 'Private')], default='friends', max_length=10),
        ),
    ]
