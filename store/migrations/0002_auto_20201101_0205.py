# Generated by Django 2.2 on 2020-10-31 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='details',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
