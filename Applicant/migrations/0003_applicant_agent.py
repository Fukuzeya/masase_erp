# Generated by Django 4.2.1 on 2023-05-26 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0001_initial'),
        ('Applicant', '0002_remove_addressdetails_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='agent_clients', to='Agent.agent'),
        ),
    ]
