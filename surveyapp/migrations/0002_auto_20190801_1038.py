# Generated by Django 2.1 on 2019-08-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
