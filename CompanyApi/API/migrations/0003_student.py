# Generated by Django 4.1 on 2024-01-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('school', models.CharField(choices=[('St Mary', 'St Mary'), ('KVIS', 'KVIS'), ('NVIS', 'NVIS')], max_length=50)),
            ],
        ),
    ]
