# Generated by Django 3.2.15 on 2022-08-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='profiles',
            field=models.ManyToManyField(related_name='profiles', to='core.Profile'),
        ),
    ]
