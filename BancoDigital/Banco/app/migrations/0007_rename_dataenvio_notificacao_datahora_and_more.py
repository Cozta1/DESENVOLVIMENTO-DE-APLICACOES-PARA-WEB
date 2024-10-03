# Generated by Django 5.1.1 on 2024-10-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_transacao_datahora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacao',
            old_name='dataEnvio',
            new_name='dataHora',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='conta',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='tipoNotificacao',
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='mensagem',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='status',
            field=models.CharField(default='pendente', max_length=20),
        ),
    ]
