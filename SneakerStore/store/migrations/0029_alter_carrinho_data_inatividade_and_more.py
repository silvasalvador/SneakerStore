# Generated by Django 4.2 on 2023-05-09 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_carrinho_data_inatividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='data_inatividade',
            field=models.DateField(default=datetime.datetime(2023, 5, 16, 16, 46, 9, 438407)),
        ),
        migrations.AlterField(
            model_name='encomenda',
            name='status',
            field=models.CharField(choices=[('Em Processamento', 'Em Processamento'), ('Cancelada', 'Cancelada'), ('Entregue', 'Entregue')], max_length=255),
        ),
    ]
