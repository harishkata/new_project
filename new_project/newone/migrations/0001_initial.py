# Generated by Django 5.0.2 on 2024-03-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
