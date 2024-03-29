# Generated by Django 4.0.4 on 2023-06-13 19:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hobbies', '0003_rename_listingsource_marketplace_itemexternalsource'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemExternalSource',
            new_name='MarketplaceItem',
        ),
        migrations.RenameField(
            model_name='marketplaceitem',
            old_name='listing_source',
            new_name='marketplace',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='date',
        ),
        migrations.AddField(
            model_name='listing',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='marketplace',
            name='data',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='universal_code_type',
            field=models.CharField(choices=[('SN', 'Set Number'), ('IS', 'ISBN'), ('CN', 'Card Number'), ('UP', 'UPC')], default=None, max_length=2),
        ),
    ]
