# Generated by Django 4.0.4 on 2022-05-22 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0007_alter_examregistration_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='examregistration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
