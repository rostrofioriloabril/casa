# Generated by Django 4.0.6 on 2022-08-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField()),
                ('dob', models.TextField()),
                ('address', models.TextField()),
                ('type_customer', models.TextField()),
                ('saldo', models.IntegerField()),
                ('branch_id', models.IntegerField()),
            ],
        ),
    ]
