# Generated by Django 4.1.2 on 2022-11-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='photo',
            field=models.URLField(blank=True, default='http://cdn.onlinewebfonts.com/svg/img_569204.png', help_text='Introduce la url de tu foto'),
        ),
    ]