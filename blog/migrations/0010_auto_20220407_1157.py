# Generated by Django 3.2.6 on 2022-04-07 09:57

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220327_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['value']},
        ),
        migrations.AddField(
            model_name='post',
            name='hero_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='hero_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(blank=True, default='0.5x0.5', editable=False, max_length=20, null=True),
        ),
    ]
