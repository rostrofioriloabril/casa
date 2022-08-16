# Generated by Django 4.1 on 2022-08-16 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('type_account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_account_name', models.TextField()),
            ],
            options={
                'db_table': 'Tipo_cuenta',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': False},
        ),
    ]
