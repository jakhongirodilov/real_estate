# Generated by Django 5.0 on 2023-12-19 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0003_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Listing Image', 'verbose_name_plural': 'Listing Images'},
        ),
    ]
