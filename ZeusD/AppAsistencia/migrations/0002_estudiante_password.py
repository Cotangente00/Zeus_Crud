# Generated by Django 5.0.6 on 2024-05-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAsistencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='password',
            field=models.CharField(max_length=100, null=True, verbose_name='Contraseña'),
        ),
    ]
