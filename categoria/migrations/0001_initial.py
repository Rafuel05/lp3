# Generated by Django 5.1.7 on 2025-04-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nome', models.CharField(max_length=80, unique=True)),
                ('categoria_imagem', models.ImageField(blank=True, upload_to='fotos/categorias')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('categoria_descricao', models.TextField(blank=True, max_length=250)),
            ],
        ),
    ]
