# Generated by Django 2.2.6 on 2020-03-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0006_fritas_saladas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastel',
            name='Tipo_Pastel',
            field=models.CharField(choices=[('Italiano', 'Italiano'), ('Catupiri', 'Catupiri'), ('Frango', 'Frango'), ('Carne', 'Carne'), ('Pizza', 'Pizza')], default='Carne', max_length=15, verbose_name='Escolha o tipo:'),
        ),
    ]
