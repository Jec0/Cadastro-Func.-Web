# Generated by Django 3.2.25 on 2024-12-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20241215_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default=0, max_length=11, unique=True),
            preserve_default=False,
        ),
    ]