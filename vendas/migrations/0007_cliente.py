# Generated by Django 3.1.7 on 2021-03-29 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_venda_produtos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
    ]
