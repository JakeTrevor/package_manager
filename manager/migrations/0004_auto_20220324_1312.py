# Generated by Django 2.2.26 on 2022-03-24 13:12

from django.db import migrations, models
import manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20220324_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='readme',
            field=models.FileField(upload_to=manager.models.Package.getUploadDir),
        ),
    ]