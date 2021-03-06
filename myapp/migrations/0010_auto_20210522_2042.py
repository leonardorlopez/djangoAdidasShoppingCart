# Generated by Django 3.0.5 on 2021-05-22 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20201213_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cursos', to='myapp.Profesor'),
        ),
    ]
