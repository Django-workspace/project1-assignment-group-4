# Generated by Django 4.0.5 on 2022-07-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist_app', '0004_comment_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='comment image'),
        ),
    ]