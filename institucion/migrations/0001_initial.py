# Generated by Django 4.1.1 on 2022-10-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complejo_deportivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_complejo', models.CharField(max_length=50)),
                ('tipo_deporte', models.CharField(max_length=50)),
                ('id_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_deporte', models.CharField(max_length=50)),
                ('nombre_escuela', models.CharField(max_length=50)),
                ('horario', models.DateField()),
                ('id_profesores', models.IntegerField()),
                ('logros', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_profesores', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('contrasenna', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
    ]