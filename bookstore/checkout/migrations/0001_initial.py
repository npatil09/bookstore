# Generated by Django 5.1 on 2024-10-19 07:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=10)),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('shipping_address', models.TextField(max_length=1500)),
                ('amount_paid', models.IntegerField(default=0)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('shipped', models.BooleanField(default=False)),
                ('date_shipped', models.DateTimeField(blank=True, null=True)),
                ('placed', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=False)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('book_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.books')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]