# Generated by Django 5.1 on 2024-10-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_codigoinv', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('marca', models.CharField(max_length=80)),
                ('modelo', models.CharField(max_length=80)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'inventario',
                'verbose_name_plural': 'inventarios',
            },
        ),
    ]
