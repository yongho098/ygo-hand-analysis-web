# Generated by Django 4.2.5 on 2023-09-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decklist', '0006_alter_decklist_deck_combo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decklist',
            name='deck_combo',
            field=models.TextField(),
        ),
    ]
