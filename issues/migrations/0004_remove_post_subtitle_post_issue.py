# Generated by Django 5.1 on 2024-09-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_rename_body_post_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='post',
            name='issue',
            field=models.CharField(default='Default Issue', max_length=128),
        ),
    ]
