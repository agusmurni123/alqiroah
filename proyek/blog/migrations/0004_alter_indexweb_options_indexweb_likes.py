# Generated by Django 5.0.3 on 2024-04-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_indexweb_tanggal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexweb',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='indexweb',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
