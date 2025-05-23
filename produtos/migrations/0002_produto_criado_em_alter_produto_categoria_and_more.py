# Generated by Django 5.1.7 on 2025-04-16 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='esta_disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
