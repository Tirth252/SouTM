# Generated by Django 3.1.6 on 2021-03-27 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210323_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.server'),
        ),
    ]
