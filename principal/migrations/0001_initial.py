# Generated by Django 4.2.4 on 2023-09-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.IntegerField()),
                ('imagen', models.URLField(blank=True, null=True)),
                ('genero', models.CharField(choices=[('Caballero', 'Caballero'), ('Dama', 'Dama'), ('Unisex', 'Unisex'), ('Niños', 'Niños')], max_length=20)),
                ('categoria', models.ForeignKey(on_delete=models.SET('NULL'), to='principal.categoria')),
            ],
        ),
    ]
