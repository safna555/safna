# Generated by Django 5.1.3 on 2024-12-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0006_alter_register_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='image',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]