# Generated by Django 3.2.8 on 2021-11-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_usertags_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertags',
            name='profile_image',
            field=models.ImageField(default='', upload_to='static/images/%y'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertags',
            name='status',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
