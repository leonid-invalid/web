# Generated by Django 2.2.7 on 2019-12-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20191207_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
