# Generated by Django 5.1.1 on 2024-10-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_endereco_options_alter_endereco_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='', max_length=11, unique=True, verbose_name='Telefone'),
        ),
    ]
