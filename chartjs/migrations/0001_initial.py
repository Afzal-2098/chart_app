# Generated by Django 4.1.3 on 2022-11-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=120)),
                ('rank', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
