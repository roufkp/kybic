# Generated by Django 4.2.1 on 2023-06-19 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_remove_testimonials_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='paragraph',
            field=models.TextField(blank=True, null=True),
        ),
    ]