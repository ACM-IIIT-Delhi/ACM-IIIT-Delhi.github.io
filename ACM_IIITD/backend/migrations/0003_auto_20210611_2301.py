# Generated by Django 3.1.7 on 2021-06-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210611_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='content',
            field=models.TextField(),
        ),
    ]
