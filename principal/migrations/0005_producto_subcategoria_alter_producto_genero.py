# Generated by Django 4.2.4 on 2023-09-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_alter_categoria_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.CharField(choices=[('Abrigos', 'Abrigos'), ('Pantalones', 'Pantalones'), ('Deportivos', 'Deportivos')], default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='genero',
            field=models.CharField(choices=[('Caballero', 'Caballero'), ('Dama', 'Dama'), ('Unisex', 'Unisex'), ('Niños', 'Niños')], max_length=100),
        ),
    ]
