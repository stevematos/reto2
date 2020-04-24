# Generated by Django 3.0.5 on 2020-04-24 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('id_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elearning.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProgressVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes_daily_play', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('dia', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('id_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elearning.Category')),
                ('id_inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Inscription')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.User'),
        ),
    ]