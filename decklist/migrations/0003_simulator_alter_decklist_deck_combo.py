# Generated by Django 4.2.5 on 2023-09-22 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decklist', '0002_rename_deck_item_decklist_deck_plaintext_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='decklist',
            name='deck_combo',
            field=models.TextField(),
        ),
    ]
