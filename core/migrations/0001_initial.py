# Generated by Django 4.0.4 on 2022-04-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('email', models.CharField(max_length=32, null=True)),
                ('phone', models.CharField(max_length=32, null=True)),
            ],
        ),
    ]
