# Generated by Django 3.2.15 on 2022-08-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_booking_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')], default='lunch', max_length=100),
        ),
    ]
