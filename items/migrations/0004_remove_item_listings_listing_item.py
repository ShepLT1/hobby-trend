# Generated by Django 4.0.4 on 2023-03-12 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_item_universal_codes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='listings',
        ),
        migrations.AddField(
            model_name='listing',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listing_item', to='items.item'),
        ),
    ]