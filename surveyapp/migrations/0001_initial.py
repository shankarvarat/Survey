# Generated by Django 2.1 on 2019-08-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_cat_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=150)),
                ('option2', models.CharField(max_length=150)),
                ('option3', models.CharField(max_length=150, null=True)),
                ('option4', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='question_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_cat_name', models.CharField(max_length=80)),
                ('main_cat_name', models.ForeignKey(on_delete='CASCADE', to='surveyapp.main_category')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete='CASCADE', to='surveyapp.question_type'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_cat_name',
            field=models.ForeignKey(on_delete='CASCADE', to='surveyapp.sub_category'),
        ),
    ]
