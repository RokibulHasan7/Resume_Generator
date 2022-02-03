# Generated by Django 4.0.2 on 2022-02-02 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PDF_generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('mobile', models.PositiveIntegerField(blank=True)),
                ('degree', models.CharField(max_length=100)),
                ('varsity_name', models.CharField(max_length=100)),
                ('passing_year', models.DateField()),
                ('result', models.CharField(blank=True, max_length=10)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('skill_detail', models.TextField()),
                ('project_detail', models.TextField(blank=True)),
                ('about_detail', models.TextField(blank=True)),
                ('award_detail', models.TextField(blank=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]