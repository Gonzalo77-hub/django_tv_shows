# Generated by Django 3.2.5 on 2021-08-17 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tv', '0003_rename_book_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Release',
            field=models.DateField(blank=True, null=True),
        ),
    ]