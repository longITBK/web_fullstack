# Generated by Django 4.2.1 on 2023-10-24 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=90, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=90, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=90, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.uni')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('floor', models.CharField(choices=[('1', 'First floor'), ('2', 'Second floor'), ('3', 'Third floor'), ('4', 'Fourth floor'), ('5', 'Fifth floor')], max_length=2, null=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.building')),
            ],
        ),
    ]
