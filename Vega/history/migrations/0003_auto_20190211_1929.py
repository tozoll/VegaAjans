# Generated by Django 2.1.5 on 2019-02-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20190211_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyyears',
            name='icon',
            field=models.FileField(upload_to='history/', verbose_name='Ikon'),
        ),
    ]
