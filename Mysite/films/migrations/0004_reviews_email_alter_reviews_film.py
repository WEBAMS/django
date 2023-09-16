# Generated by Django 4.2.5 on 2023-09-16 08:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film', verbose_name='Фильм'),
        ),
    ]
