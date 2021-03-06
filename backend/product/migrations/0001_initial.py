# Generated by Django 3.2.3 on 2022-01-16 11:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Наименование товара')),
                ('type', models.IntegerField(choices=[(0, 'Продовольственные'), (1, 'Не продовольственные')], default=0)),
                ('data_delivery', models.DateTimeField(null=True, verbose_name='Значение типа дата/время')),
                ('points_of_issue', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'PRODUCT',
            },
        ),
    ]
