# Generated by Django 3.1.3 on 2020-11-22 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0003_auto_20201121_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.articulo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.cliente')),
            ],
        ),
    ]
