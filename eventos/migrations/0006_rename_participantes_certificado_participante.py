# Generated by Django 4.2 on 2023-04-22 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_certificado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='participantes',
            new_name='participante',
        ),
    ]
