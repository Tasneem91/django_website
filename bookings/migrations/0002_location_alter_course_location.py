# Generated by Django 4.2.1 on 2023-05-30 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.location'),
        ),
    ]
