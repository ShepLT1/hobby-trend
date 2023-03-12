# Generated by Django 4.0.4 on 2023-03-12 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_remove_hobby_listing_sources_remove_listing_media_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection_groups', '0002_alter_collectionitem_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='hobby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='collection_hobby', to='items.hobby'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='collectionitem',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='collection_groups.collection'),
        ),
        migrations.AlterField(
            model_name='collectionitem',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='items.item'),
        ),
    ]
