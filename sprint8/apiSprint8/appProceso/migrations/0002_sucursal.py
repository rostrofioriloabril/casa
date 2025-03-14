# Generated by Django 4.0.6 on 2022-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProceso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address', models.TextField()),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
    ]
