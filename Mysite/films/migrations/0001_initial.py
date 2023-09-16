# Generated by Django 4.2.5 on 2023-09-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imag', models.ImageField(upload_to='image/%Y')),
                ('description', models.TextField(blank=True)),
                ('date_publ', models.DateField(verbose_name='Дата выхода')),
            ],
        ),
    ]