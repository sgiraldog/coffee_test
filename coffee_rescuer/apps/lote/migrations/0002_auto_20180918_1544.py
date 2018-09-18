# Generated by Django 2.1.1 on 2018-09-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallelote',
            name='etapa_hongo',
            field=models.PositiveIntegerField(choices=[(0, 'Etapa 0'), (1, 'Etapa 1'), (2, 'Etapa 2'), (3, 'Etapa 3'), (4, 'Etapa 4')], default=0),
        ),
        migrations.AlterField(
            model_name='lote',
            name='ultimo_estado_hongo',
            field=models.PositiveIntegerField(choices=[(0, 'Etapa 0'), (1, 'Etapa 1'), (2, 'Etapa 2'), (3, 'Etapa 3'), (4, 'Etapa 4')], default=0),
        ),
    ]