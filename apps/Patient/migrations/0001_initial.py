# Generated by Django 5.0.2 on 2024-03-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], max_length=1, verbose_name='Пол')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Рост')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
    ]
