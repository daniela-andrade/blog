# Generated by Django 4.0 on 2021-12-23 15:19

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to='profiles'),
            preserve_default=False,
        ),
    ]
