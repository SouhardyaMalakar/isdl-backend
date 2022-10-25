# Generated by Django 4.1.2 on 2022-10-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_actor_datetime_hall_requests_delete_tempmodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DateTime',
            new_name='Booking',
        ),
        migrations.DeleteModel(
            name='Requests',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='actor_booked',
        ),
        migrations.RemoveField(
            model_name='hall',
            name='hall_selectedslots',
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_bookings',
            field=models.ManyToManyField(through='restapi.Booking', to='restapi.hall'),
        ),
    ]
