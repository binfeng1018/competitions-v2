# Generated by Django 2.1.2 on 2018-11-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0023_auto_20181127_0329'),
        ('leaderboards', '0006_auto_20181002_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='submissions',
            field=models.ManyToManyField(to='competitions.Submission'),
        ),
    ]
