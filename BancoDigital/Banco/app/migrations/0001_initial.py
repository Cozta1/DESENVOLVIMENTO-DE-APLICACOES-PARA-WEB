# Generated by Django 5.1.1 on 2024-10-01 17:57

import app.models
import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeagencia', models.CharField(max_length=100, verbose_name='Nome da Agência')),
                ('numeroagencia', models.CharField(default='0000000000', editable=False, max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Agencia',
                'verbose_name_plural': 'Agencias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('senha', models.CharField(max_length=255, verbose_name='Senha')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True)),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=app.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(max_length=50, verbose_name='Complemento')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('numeroConta', models.CharField(default=0, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Número da Conta')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Saldo')),
                ('dataAbertura', models.DateField(auto_now_add=True, verbose_name='Data de Abertura')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agencia')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCartao', models.BigIntegerField(blank=True, unique=True, verbose_name='Numero do Cartão')),
                ('bandeira', models.CharField(choices=[('visa', 'Visa'), ('elo', 'Elo'), ('mastercard', 'MasterCard')], default='visa', max_length=20, verbose_name='Bandeira')),
                ('dataExpiracao', models.DateField(blank=True, verbose_name='Data de Expiração')),
                ('cvv', models.IntegerField(blank=True, verbose_name='CVV')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conta')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.endereco'),
        ),
        migrations.AddField(
            model_name='agencia',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.endereco'),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('idNoti', models.CharField(default=0, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='ID Notificação')),
                ('tipoNotificacao', models.CharField(choices=[('transacao confirmada', 'Transação confirmada'), ('transacao cancelada', 'Transação cancelada')], verbose_name='Tipo de Notificação')),
                ('mensagem', models.TextField()),
                ('dataEnvio', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('cliente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('numeroTransacao', models.CharField(default=0, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Número da Transação')),
                ('tipoTransacao', models.CharField(choices=[('deposito', 'Depósito'), ('saque', 'Saque'), ('transferencia', 'Transferência')], max_length=15, verbose_name='Tipo de Transação')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('dataHora', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
                ('status', models.CharField(choices=[('concluida', 'Concluída'), ('cancelada', 'Cancelada')], default='Pendente', max_length=10, verbose_name='Status')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='app.conta')),
                ('contaDestino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transferencias', to='app.conta')),
            ],
            options={
                'verbose_name': 'Transação',
                'verbose_name_plural': 'Transações',
            },
        ),
    ]
