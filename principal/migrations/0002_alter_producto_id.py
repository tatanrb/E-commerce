# Generated by Django 4.2.4 on 2023-09-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
