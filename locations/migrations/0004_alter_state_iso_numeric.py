# Generated by Django 5.0.2 on 2025-06-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_state_iso2_alter_state_iso3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='iso_numeric',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
