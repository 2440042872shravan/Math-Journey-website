# Generated by Django 2.2.10 on 2021-05-11 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0026_timeslots_workingdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslots',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='time_slot_subject', to='curriculum.Subject'),
            preserve_default=False,
        ),
    ]
