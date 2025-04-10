# Generated by Django 4.2.2 on 2023-06-28 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
                ('medidas', models.CharField(max_length=60)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.marca')),
            ],
        ),
    ]
