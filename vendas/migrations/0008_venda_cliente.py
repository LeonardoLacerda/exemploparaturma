# Generated by Django 3.1.7 on 2021-03-29 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0007_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.cliente'),
        ),
    ]
