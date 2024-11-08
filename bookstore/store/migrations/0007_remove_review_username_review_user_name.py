# Generated by Django 5.1 on 2024-10-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_review_user_name_review_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='username',
        ),
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]