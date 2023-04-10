# Generated by Django 4.0.4 on 2023-04-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_alter_item_sets_alter_item_variations_and_more'),
        ('collection_groups', '0004_remove_collectionitem_condition_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitem',
            name='condition',
            field=models.ManyToManyField(default=[1], related_name='condition', to='collection_groups.condition'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='hobby',
            field=models.ManyToManyField(default=[1], related_name='condition_hobby', to='items.hobby'),
        ),
    ]