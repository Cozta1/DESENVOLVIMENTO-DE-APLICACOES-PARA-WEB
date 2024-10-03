# Generated by Django 5.1.1 on 2024-10-03 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_notificacao_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cliente'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='status',
            field=models.CharField(choices=[('concluida', 'Concluída'), ('cancelada', 'Cancelada')], default='pendente', editable=False, max_length=10, verbose_name='Status'),
        ),
    ]
