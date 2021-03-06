# Generated by Django 2.0.4 on 2018-04-17 20:19

import apps.todo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('TDO', 'Por Hacer'), ('DNG', 'Haciendo'), ('DNE', 'Hecho')], max_length=3)),
                ('position', models.PositiveSmallIntegerField()),
                ('priority', apps.todo.models.IntegerRangeField()),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
        ),
    ]
