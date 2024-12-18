# Generated by Django 5.1.1 on 2024-11-25 00:09

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import stdimage.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('nomeagencia', models.CharField(max_length=100, verbose_name='Nome da Agência')),
                ('numeroagencia', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Agência',
                'verbose_name_plural': 'Agências',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('CPF', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='CPF')),
                ('telefone', models.CharField(default='', max_length=11, unique=True, verbose_name='Telefone')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='clientes/', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('numeroConta', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Número da Conta')),
                ('dataAbertura', models.DateField(auto_now_add=True, verbose_name='Data de Abertura')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agencia')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('numeroCartao', models.BigIntegerField(blank=True, editable=False, unique=True, verbose_name='Numero do Cartão')),
                ('bandeira', models.CharField(choices=[('visa', 'Visa'), ('elo', 'Elo'), ('mastercard', 'MasterCard')], default='visa', max_length=20, verbose_name='Bandeira')),
                ('dataExpiracao', models.DateField(blank=True, editable=False, verbose_name='Data de Expiração')),
                ('cvv', models.IntegerField(blank=True, editable=False, verbose_name='CVV')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conta')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
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
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.AddField(
            model_name='agencia',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.endereco'),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
                ('dataHora', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificacoes', to='app.conta')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('numeroTransacao', models.AutoField(primary_key=True, serialize=False, verbose_name='Número da Transação')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('tipoTransacao', models.CharField(choices=[('deposito', 'Depósito'), ('saque', 'Saque'), ('transferencia', 'Transferência')], max_length=50, verbose_name='Tipo de Transação')),
                ('status', models.CharField(default='pendente', editable=False, max_length=20, verbose_name='Status')),
                ('dataHora', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data e Hora da Transação')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='app.conta')),
                ('contaDestino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transacoes_destino', to='app.conta')),
            ],
            options={
                'verbose_name': 'Transação',
                'verbose_name_plural': 'Transações',
            },
        ),
    ]
