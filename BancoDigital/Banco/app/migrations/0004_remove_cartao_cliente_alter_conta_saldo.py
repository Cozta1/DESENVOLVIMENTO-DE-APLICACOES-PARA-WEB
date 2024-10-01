# Generated by Django 5.1.1 on 2024-10-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cartao_cvv_alter_cartao_dataexpiracao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartao',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='conta',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Saldo'),
        ),
    ]
