# Generated by Django 2.1.2 on 2019-01-28 23:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0005_auto_20181002_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='key',
            field=models.UUIDField(blank=True, default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='type',
            field=models.CharField(choices=[('ingestion_program', 'Ingestion Program'), ('input_data', 'Input Data'), ('public_data', 'Public Data'), ('reference_data', 'Reference Data'), ('scoring_program', 'Scoring Program'), ('starting_kit', 'Starting Kit'), ('competition_bundle', 'Competition Bundle'), ('submission', 'Submission'), ('solution', 'Solution')], max_length=64),
        ),
    ]
