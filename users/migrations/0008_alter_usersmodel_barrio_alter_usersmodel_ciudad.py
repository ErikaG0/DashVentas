# Generated by Django 5.0.3 on 2024-04-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_usersmodel_barrio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='barrio',
            field=models.CharField(choices=[('barrioB1', 'Chapinero'), ('barrioB2', 'Usaquen'), ('barrioB3', 'Suba'), ('barrioB4', 'Kennedy'), ('barrioB5', 'Usme')], max_length=100),
        ),
        migrations.AlterField(
            model_name='usersmodel',
            name='ciudad',
            field=models.CharField(default='Bogota', max_length=40),
        ),
    ]
