# Generated by Django 4.2.9 on 2024-02-04 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_rename_repuestos_cursos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]
