# Generated by Django 5.0.6 on 2024-07-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total']},
        ),
    ]
