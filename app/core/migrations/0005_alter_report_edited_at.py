# Generated by Django 3.2.15 on 2022-08-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_report_edited_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='edited_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
