# Generated by Django 2.2.17 on 2020-12-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_testing'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='gjhg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
