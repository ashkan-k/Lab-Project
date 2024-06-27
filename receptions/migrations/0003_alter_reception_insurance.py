# Generated by Django 5.0.6 on 2024-06-25 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0001_initial'),
        ('receptions', '0002_alter_medicaltest_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='insurance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurances.insurance', verbose_name='بیمه'),
        ),
    ]