# Generated by Django 2.1.2 on 2018-10-13 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HoneyPot', '0006_auto_20181013_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connex',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='connex',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='connex',
            name='user_agent',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_agent',
            field=models.TextField(max_length=50),
        ),
    ]
