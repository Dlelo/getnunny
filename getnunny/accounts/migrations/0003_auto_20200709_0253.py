# Generated by Django 3.0.4 on 2020-07-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200708_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nunny',
            name='pay_range',
            field=models.FloatField(blank=True, null=True),
        ),
    ]