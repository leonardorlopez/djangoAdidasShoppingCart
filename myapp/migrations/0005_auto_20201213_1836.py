# Generated by Django 3.1.3 on 2020-12-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_curso_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='turno',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Noche'), (1, 'Mañana'), (2, 'Tarde')], null=True, verbose_name='Turno'),
        ),
    ]
