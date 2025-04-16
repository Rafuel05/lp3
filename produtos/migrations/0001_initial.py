# Generated by Django 5.1.7 on 2025-04-10 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_nome', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=210, unique=True)),
                ('descricao', models.TextField(max_length=300)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('imagens', models.ImageField(blank=True, upload_to='fotos/produtos')),
                ('estoque', models.IntegerField()),
                ('esta_disponivel', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria')),
            ],
        ),
    ]
