# Generated by Django 4.1 on 2022-08-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_alter_cliente_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dob',
            field=models.DateTimeField(),
        ),
    ]
