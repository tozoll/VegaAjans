# Generated by Django 2.1.5 on 2019-02-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyyears',
            name='icon',
            field=models.FileField(upload_to='', verbose_name='Ikon'),
        ),
    ]