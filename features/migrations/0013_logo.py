# Generated by Django 4.0.4 on 2022-05-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0012_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('header', models.ImageField(null=True, upload_to='logo_images/header')),
                ('footer_logo', models.ImageField(null=True, upload_to='logo_images/footer')),
            ],
        ),
    ]