# Generated by Django 4.2.1 on 2023-06-19 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_testimonials_paragraph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonials',
            name='created_at',
        ),
    ]
