# Generated by Django 2.2.6 on 2019-12-15 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=70)),
                ('ciudad', models.CharField(max_length=30)),
                ('comuna', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('folio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
                ('idascensor', models.IntegerField()),
                ('modeloasc', models.CharField(max_length=30)),
                ('fallas', models.CharField(blank=True, max_length=200, null=True)),
                ('reparaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('piezascambiadas', models.CharField(blank=True, max_length=100, null=True)),
                ('receptor', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(db_column='nombre', on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.tecnico')),
            ],
        ),
    ]
