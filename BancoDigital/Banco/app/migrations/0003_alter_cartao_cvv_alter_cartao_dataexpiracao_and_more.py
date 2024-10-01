# Generated by Django 5.1.1 on 2024-10-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_endereco_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartao',
            name='cvv',
            field=models.IntegerField(blank=True, editable=False, verbose_name='CVV'),
        ),
        migrations.AlterField(
            model_name='cartao',
            name='dataExpiracao',
            field=models.DateField(blank=True, editable=False, verbose_name='Data de Expiração'),
        ),
        migrations.AlterField(
            model_name='cartao',
            name='numeroCartao',
            field=models.BigIntegerField(blank=True, editable=False, unique=True, verbose_name='Numero do Cartão'),
        ),
        migrations.AlterField(
            model_name='conta',
            name='numeroConta',
            field=models.CharField(default=0, editable=False, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Número da Conta'),
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='idNoti',
            field=models.CharField(default=0, editable=False, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='ID Notificação'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='numeroTransacao',
            field=models.CharField(default=0, editable=False, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Número da Transação'),
        ),
    ]