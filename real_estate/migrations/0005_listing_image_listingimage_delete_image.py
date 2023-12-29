# Generated by Django 5.0 on 2023-12-19 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0004_alter_image_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='listing_images/')),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='real_estate.listing')),
            ],
            options={
                'verbose_name': 'Listing Image',
                'verbose_name_plural': 'Listing Images',
            },
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
