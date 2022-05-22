# Generated by Django 4.0.4 on 2022-05-20 18:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='participants',
            field=models.ManyToManyField(related_name='modules', to=settings.AUTH_USER_MODEL),
        ),
    ]